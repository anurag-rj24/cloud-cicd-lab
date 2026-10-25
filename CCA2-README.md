# 🚀 Cloud CI/CD Pipeline Implementation & Deployment (CCA 2)

Automated end-to-end CI/CD delivery pipeline implementing **GitHub**, **Jenkins**, **Docker**, **Docker Hub**, and **Kubernetes (Minikube)** on **AWS EC2**.

- **Student Name:** Anurag
- **Course:** TYCSE: Cloud Computing and DevOps
- **Project:** Cloud CI/CD Microservice Web Application
- **GitHub Repository:** [anurag-rj24/cloud-cicd-lab](https://github.com/anurag-rj24/cloud-cicd-lab)
- **Container Registry:** Docker Hub (`anuragrj24/cloud-cicd-app`)
- **Deployment Platform:** Minikube Kubernetes on AWS EC2 (Ubuntu 22.04 LTS, ap-south-1 Mumbai)

---

## 📌 1. Pipeline Overview & Architecture

The pipeline automates continuous integration and continuous deployment on every code push:

```
[ Developer Git Push ]
        │
        ▼
[ GitHub Repository ]
        │  (Webhook / SCM Polling)
        ▼
[ Jenkins on AWS EC2 ] ──► Stage 1: Checkout Code
        │              ──► Stage 2: Build & Run Unit Tests (`test_app.py`)
        │              ──► Stage 3: Docker Image Build (`anuragrj24/cloud-cicd-app:${BUILD_NUMBER}`)
        │              ──► Stage 4: Docker Hub Push (with credentials binding)
        │              ──► Stage 5: Minikube Deployment (`kubectl apply & set image`)
        │              ──► Stage 6: Verification (Check Pods, Deployment, Service)
        ▼
[ Minikube Cluster ] ────► Running Pod: flask-app (NodePort 30005)
```

---

## 📂 2. Repository Structure

```
├── Jenkinsfile              # Declarative Jenkins CI/CD pipeline definition
├── Dockerfile               # Multi-stage production container specification
├── requirements.txt         # Application dependencies (Flask)
├── app.py                   # Main Flask microservice application
├── test_app.py              # Automated unit tests (4 unit tests)
├── templates/
│   └── index.html           # Modern dashboard web interface
├── k8s/
│   ├── deployment.yaml      # Kubernetes Deployment manifest with probes
│   └── service.yaml         # Kubernetes NodePort Service manifest (30005)
├── CCA2-README.md           # Submission documentation & evaluation guide
└── start-cicd.bat           # Helper batch automation script
```

---

## ⚙️ 3. Pipeline Stages Breakdown

| Stage | What Happens | Command / Tool |
| :--- | :--- | :--- |
| **1. Checkout** | Jenkins pulls the latest commit from the GitHub repository | `checkout scm` |
| **2. Build & Test** | Installs dependencies and runs automated test suite | `python3 -m unittest test_app.py` |
| **3. Docker Build** | Builds Docker image tagged with build number and `latest` | `docker build -t anuragrj24/cloud-cicd-app:${BUILD_NUMBER} .` |
| **4. Push Image** | Logs in to Docker Hub using Jenkins credentials and pushes image | `docker push anuragrj24/cloud-cicd-app:${BUILD_NUMBER}` |
| **5. Minikube Deploy** | Applies manifests and performs rolling update on cluster | `kubectl apply -f k8s/` & `kubectl rollout status` |
| **6. Verification** | Asserts pods are Running (1/1) and service endpoint is active | `kubectl get pods,svc` |

---

## 🔄 4. Demonstrating Source Code Change & Redeployment

1. **Initial Deployment (Version 1):**
   - Application displays: `VERSION = "v1.0.0"`
   - Pipeline completes successfully with build `#1`.

2. **Triggering Redeployment (Version 2):**
   - In `app.py`, update:
     ```python
     VERSION = "v1.1.0"
     PIPELINE_STATUS = "CI/CD Pipeline is Live & Running - Version 2!"
     ```
   - Commit and push to GitHub:
     ```bash
     git commit -am "chore: update app to version 2"
     git push origin main
     ```
   - Jenkins pipeline triggers automatically, executes all 6 stages, builds image `#2`, and performs a zero-downtime rolling update on Minikube.
   - Accessing the service confirms the updated version and message without manual intervention.

---

## 📊 5. Verification Commands

```bash
# Check Minikube status
minikube status

# Check running Pods
kubectl get pods -l app=flask-app

# Check Deployment rollout status
kubectl get deployment flask-app

# Access application service
minikube service flask-service --url
```
