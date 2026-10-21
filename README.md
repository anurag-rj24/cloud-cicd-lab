# 🚀 Cloud CI/CD Pipeline with Kubernetes (Minikube)

Automated end-to-end CI/CD pipeline built with **Flask**, **Docker**, **Kubernetes (Minikube)**, and **GitHub Actions Self-Hosted Runner**.

**Developer:** Anurag  
**GitHub Repository:** [anurag-rj24/cloud-cicd-lab](https://github.com/anurag-rj24/cloud-cicd-lab)  
**Live Endpoint:** `http://127.0.0.1:51252` (or `minikube service flask-service`)

---

## 🏗️ Architecture & Pipeline Flow

```
   [ GitHub Repository ]
            │
            ▼ (Commit / Push to 'main')
   [ GitHub Actions CI ]  ➜ Cloud syntax check & image test
            │
            ▼ (Triggers Local Self-Hosted Runner)
   [ Local Docker Daemon ] ➜ Builds `flask-app:latest`
            │
            ▼
   [ Minikube Cluster ]   ➜ `minikube image load flask-app:latest`
            │
            ▼
   [ Kubernetes Deploy ]  ➜ `kubectl apply -f k8s/deployment.yaml`
                          ➜ `kubectl rollout restart deployment/flask-app`
            │
            ▼
   [ Live Application ]   ➜ Running at NodePort 30005
```

---

## 📋 Demonstration Steps for Evaluator / Teacher

1. **Verify Current Status:**
   - Open browser at `http://127.0.0.1:51252`
   - Notice developer name **Anurag** and version `v1.0.0`.

2. **Trigger Automated CI/CD from GitHub:**
   - Go to [github.com/anurag-rj24/cloud-cicd-lab/edit/main/app.py](https://github.com/anurag-rj24/cloud-cicd-lab/edit/main/app.py).
   - Change `VERSION = "v1.0.1"` or update the `MESSAGE` string.
   - Click **Commit changes**.

3. **Observe Automated Pipeline:**
   - Watch the GitHub Actions tab: [Actions Workflow Run](https://github.com/anurag-rj24/cloud-cicd-lab/actions)
   - Cloud CI validates the code.
   - Local runner builds the container and rolls out the deployment to Minikube.

4. **Verify Live Deployment:**
   - Refresh `http://127.0.0.1:51252` — the new version and message appear automatically without any manual intervention!
