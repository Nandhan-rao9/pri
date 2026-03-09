# The project onitors AWS services continuously and highlights security risks through a modern visual dashboard.

---

## 🚀 Features

### 🔹 Real-Time Security Monitoring

* Event-driven detection using AWS CloudTrail and EventBridge
* No polling or scheduled scans
* Immediate detection of risky configuration changes

### 🔹 Targeted Misconfiguration Detection

Scans only the affected resources when an event occurs:

* **EC2**

  * Publicly exposed security groups
  * Sensitive ports open (22, 3389)
  * Instances with public IP
  * IMDSv1 enabled
  * Unencrypted EBS volumes

* **S3**

  * Public bucket policies
  * Public ACLs
  * Block Public Access disabled
  * Encryption disabled

* **IAM**

  * Overly permissive policies
  * Wildcard permissions

---

### 🔹 Finding Lifecycle Tracking

Each vulnerability follows a lifecycle model:

```
OPEN → RESOLVED
```

Findings are never deleted, enabling:

* Historical risk analysis
* Audit trails
* Resolution tracking
* Future risk scoring

---

### 🔹 Security Dashboard

Modern animated dashboard provides:

* Open vs Resolved findings
* Severity distribution
* Service impact breakdown
* Risk score calculation
* Priority-sorted vulnerabilities
* Drill-down modal for deep inspection

---

### 🔹 Inventory Visibility

Full infrastructure inventory across:

* EC2 instances
* Security groups
* S3 buckets
* IAM users
* IAM roles

---

# 🏗 System Architecture

```
AWS API Call
    ↓
CloudTrail logs event
    ↓
EventBridge Rule
    ↓
API Destination (HTTPS)
    ↓
Flask Backend
    ↓
Targeted Security Scanner
    ↓
MongoDB Atlas (Findings Lifecycle)
    ↓
React Dashboard
```

---

# 🧰 Tech Stack

## Backend

* Python
* Flask
* Boto3
* MongoDB Atlas
* AWS CloudTrail
* AWS EventBridge
* AWS API Destinations

## Frontend

* React (Vite)
* Tailwind CSS
* Framer Motion
* Recharts
* Zustand

---

# 📂 Project Structure

```
clousec/
│
├── backend/
│   └── app.py
│
├── clousec/
│   ├── scanners/
│   ├── models/
│   ├── services/
│   └── utils/
│
└── frontend/
    └── (React App)
```

---

# ⚙ Backend Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If missing:

```bash
pip install flask flask-cors boto3 pymongo python-dotenv
```

---

### 3️⃣ Configure Environment

Create `.env` file:

```
MONGO_URI=your_mongodb_connection_string
```

---

### 4️⃣ Run Backend

From project root:

```bash
set PYTHONPATH=.
python -m backend.app
```

Backend runs on:

```
http://localhost:5000
```

Health check:

```
http://localhost:5000/health
```

---

# 🌐 Frontend Setup

### 1️⃣ Install Dependencies

```bash
cd frontend
npm install
```

### 2️⃣ Run Dev Server

```bash
npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🔐 API Endpoints

### Health

```
GET /health
```

### Dashboard Summary

```
GET /dashboard
```

### Findings

```
GET /findings
GET /findings?status=OPEN
```

### Inventory

```
GET /inventory
```

### Event Receiver

```
POST /event
```

---

# 🧠 Risk Scoring Model

Severity weights:

| Severity | Weight |
| -------- | ------ |
| CRITICAL | 5      |
| HIGH     | 3      |
| MEDIUM   | 1      |

Risk Score Formula:

```
Total Risk = Σ(severity_weight × count)
```

---

# 🎯 Key Capabilities

* Event-driven cloud security
* Lifecycle-aware vulnerability tracking
* Priority-based alerting
* Historical risk visibility
* Real-time dashboard insights
* Scalable CSPM foundation

---



Tell me what you want next.
