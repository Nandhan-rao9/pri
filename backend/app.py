from clousec.utils.db import findings_collection
from flask import Flask, jsonify
from clousec.scanners.s3_scanner import scan_s3_buckets
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "ClouSec backend running"})

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
    app.run(debug=True, host="0.0.0.0", port=5000)