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
