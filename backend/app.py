from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from clousec.scanners.ec2_scanner import scan_security_groups

from clousec.utils.db import findings_collection
from clousec.scanners.s3_scanner import scan_s3_buckets

app = Flask(__name__)

def start_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=scan_s3_buckets,
        trigger="interval",
        minutes=2,
        id="s3_scan_job",
        replace_existing=True,
    )

    scheduler.add_job(
        func=scan_security_groups,
        trigger="interval",
        minutes=2,
        id="ec2_sg_scan_job",
        replace_existing=True,
    )

    scheduler.start()
    print("⏰ Scheduler started (S3 + EC2 scans every 2 minutes)")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/scan/s3")
def scan_s3():
    scan_s3_buckets()
    return jsonify({"message": "S3 scan completed"})


@app.route("/findings")
def get_findings():
    findings = list(findings_collection.find({}, {"_id": 0}))
    return jsonify(findings)

if __name__ == "__main__":
    print("🚀 Starting ClouSec backend...")
    start_scheduler()
    app.run(debug=True, host="0.0.0.0", port=5000)