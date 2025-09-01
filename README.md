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

