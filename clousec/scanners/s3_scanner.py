import boto3
from datetime import datetime
from clousec.utils.db import findings_collection

s3 = boto3.client("s3")


def is_bucket_public(bucket_name):
    """Check if S3 bucket is public"""

    try:
        status = s3.get_bucket_policy_status(Bucket=bucket_name)
        return status["PolicyStatus"]["IsPublic"]
    except Exception:
        return False


def scan_s3_buckets():
    """Scan all buckets and store findings"""

    print("🔍 Scanning S3 buckets...")

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        bucket_name = bucket["Name"]

        is_public = is_bucket_public(bucket_name)

        if is_public:
            finding = {
                "service": "S3",
                "resource_id": bucket_name,
                "severity": "HIGH",
                "issue": "Public S3 bucket detected",
                "region": "global",
                "timestamp": datetime.utcnow()
            }

            findings_collection.insert_one(finding)
            print(f"🚨 Public bucket found: {bucket_name}")

    print("✅ S3 scan complete")