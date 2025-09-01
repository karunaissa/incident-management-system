## 🚀 Incident Management System

- A containerized Incident Management System built with Python (Flask), containerized using Docker, and deployed on Kubernetes (Minikube).
  The application supports incident tracking, assignment, resolution, and email notifications for each step of the workflow.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 📌 Features

- User authentication (Register / Login)

- Create, assign, and resolve incidents

- Email notifications on:

- New incident created

- Incident assigned

- Incident assigned to engineer

- Incident resolved

- Kubernetes manifests for Deployment, Service, Namespace, Secrets, and Ingress

- Deployed on Minikube with kubectl port-forward for local access
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠 Tech Stack

- Backend: Python (Flask)
- Database: SQLite (can be extended to RDS/Postgres)
- Email: SMTP integration via Flask-Mail
- Containerization: Docker
- Orchestration: Kubernetes (Minikube)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure
```
incident-management/
├── app/                 # Flask app logic
│   ├── templates/       # HTML templates
│   ├── auth.py          # Authentication routes
│   ├── emails.py        # Email sending logic
│   ├── forms.py         # Flask-WTF forms
│   ├── models.py        # Database models
│   └── routes.py        # Core incident routes
├── k8s/                 # Kubernetes manifests
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── namespace.yaml
│   ├── secret.yaml
│   └── service.yaml
├── Dockerfile           # Container build file
├── requirements.txt     # Python dependencies
├── run.py               # Flask entrypoint
└── .env                 # Environment variables
   ````
------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚡ Setup & Deployment
### 1️⃣ Prerequisites
- Minikube
- kubectl
- Docker
------------------------------------------------------------------------------------------------------------
### 2️⃣ Build Docker Image
- docker build -t incident-app:latest .

### 3️⃣ Start Minikube
- minikube start

### 4️⃣ Apply Kubernetes Manifests
```
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
# Ingress is optional (may not work well on Windows)
# kubectl apply -f k8s/ingress.yaml
```

### 5️⃣ Verify Deployment
```
kubectl get pods -n incident-mgmt
kubectl get svc -n incident-mgmt
```

### 6️⃣ Port Forward the Service (Recommended for Windows users)
- kubectl port-forward svc/incident-app-service -n incident-mgmt 5000:80
--------------------------------------------------------------------------------------------------------------------
## Now open in browser:
-  👉 http://localhost:5000

### 📧 Email Notifications

- Configured via environment variables (.env file). Example:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```
### 🧪 Demo Flow

- Register a new user and login

- Create a new incident → 📩 Email notification sent

- Assign the incident to an engineer → 📩 Email notification sent

- Resolve the incident → 📩 Email notification sent

### ⚠️ Notes

- On Windows, Ingress & minikube tunnel may not work reliably → use kubectl port-forward.

- Default database is SQLite (instance/site.db) for simplicity.

- For production, switch to PostgreSQL/MySQL and use a managed Kubernetes cluster.

### 📌 Future Enhancements

- Integrate Prometheus & Grafana for monitoring

- CI/CD pipeline with GitHub Actions / Jenkins

- Helm chart for deployment

- Extend database to Postgres with persistence
