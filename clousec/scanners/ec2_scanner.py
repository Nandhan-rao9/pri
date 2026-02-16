import boto3
from datetime import datetime
from clousec.utils.db import findings_collection

from clousec.utils.aws_regions import get_all_regions

SENSITIVE_PORTS = {22, 3389}


def is_world_open(permission):
    """Check if rule allows 0.0.0.0/0"""
    for ip_range in permission.get("IpRanges", []):
        if ip_range.get("CidrIp") == "0.0.0.0/0":
            return True
    return False


def scan_security_groups():
    print("🔍 Scanning EC2 security groups across regions...")

    regions = get_all_regions()

    for region in regions:
        print(f"🌍 Checking region: {region}")

        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_security_groups()

        for sg in response["SecurityGroups"]:
            sg_id = sg["GroupId"]

            for perm in sg.get("IpPermissions", []):
                from_port = perm.get("FromPort")
                to_port = perm.get("ToPort")

                if is_world_open(perm):

                    severity = "MEDIUM"

                    if from_port in SENSITIVE_PORTS:
                        severity = "HIGH"

                    if from_port == 0 and to_port == 65535:
                        severity = "CRITICAL"

                    finding = {
                        "service": "EC2",
                        "resource_id": sg_id,
                        "severity": severity,
                        "issue": "Security group open to world",
                        "region": region,
                        "timestamp": datetime.utcnow(),
                    }

                    findings_collection.update_one(
                        {
                            "service": "EC2",
                            "resource_id": sg_id,
                            "issue": "Security group open to world",
                            "region": region,
                        },
                        {"$set": finding},
                        upsert=True,
                    )

                    print(f"🚨 Open security group found: {sg_id} ({region})")

    print("✅ EC2 multi-region scan complete")