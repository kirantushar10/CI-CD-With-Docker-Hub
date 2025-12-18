## 🚀 CI/CD Pipeline for Dockerized Flask Application
<div align="center">

🚀✨ *A complete CI/CD pipeline for a Dockerized Flask application using GitHub Actions* ✨🚀  
Build • Test • Containerize • Deploy — fully automated with modern DevOps practices

---

### 🌶️ **Flask** • 🧪 **Pytest** • 🐳 **Docker** • 🤖 **GitHub Actions** • 📦 **Docker Hub**

![Static Badge](https://img.shields.io/badge/Python-3.10+-blue)
![Static Badge](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![Static Badge](https://img.shields.io/badge/Pytest-Testing-green?logo=pytest)
![Static Badge](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Static Badge](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions)
![Static Badge](https://img.shields.io/badge/Docker_Hub-Image_Registry-2496ED?logo=docker)
![Static Badge](https://img.shields.io/badge/Status-Active-brightgreen)

🔗 **GitHub Repository:**  
https://github.com/kirantushar10/CI-CD-With-Docker-Hub

</div>

---

## 🌟 Overview
*This project demonstrates a fully automated CI/CD pipeline for a Dockerized Flask application, built using modern DevOps tools and best practices:*

- 🌶️ **Flask** for building a lightweight web application
- 🧪 **Pytest** for automated testing and validation
- 🐳 **Docker** for containerizing the application
- 🤖 **GitHub** Actions for continuous integration and continuous deployment
- 📦 **Docker** Hub for storing and distributing Docker images

*The pipeline automatically tests, builds, and deploys the application whenever changes are pushed to the main branch, ensuring reliable, consistent, and production-ready deployments.*

---

## 📁 Project Structure

```bash
.
├── .github/
│   └── workflows/
│       └── cicd.yml        # 🤖 GitHub Actions pipeline
├── app.py                 # 🌶️ Flask application
├── test_app.py            # 🧪 Pytest test cases
├── requirements.txt       # 📦 Python dependencies
├── DockerFile             # 🐳 Docker build config
├── README.md              # 📘 Documentation
└── .gitignore

```

---
## 🌶️ Flask Application

This project uses a minimal Flask web application that exposes a single HTTP endpoint (/). When accessed, it returns a simple response, making it ideal for demonstrating containerization and CI/CD workflows without unnecessary complexity. The application runs on port 5000 and is configured to work seamlessly inside a Docker container.

## 🧪 Testing with Pytest

Pytest is used to validate the application behavior automatically during the CI pipeline.

The test ensures:

- ✅ The application starts correctly

- ✅ The root endpoint (/) responds successfully

- ✅ The returned response matches the expected output

This guarantees that only tested and verified code proceeds to the Docker build stage.

## 🐳 Docker Configuration

The application is fully containerized using Docker, ensuring consistency across environments.

Key highlights:

- 📦 Uses a lightweight Python base image

- ⚙️ Installs required dependencies

- 🔓 Exposes port 5000 for external access

- ▶️ Automatically starts the Flask app when the container runs

Docker enables portable deployment and smooth integration with the CI/CD pipeline.

---

## 🤖 CI/CD Pipeline

### *🧪 Job 1: Build & Test (Continuous Integration)*
```bash
A[👨‍💻 Code Push / Pull Request] --> B[🤖 GitHub Actions Triggered] --> C[🧪 Job 1: Build & Test]
```
### *🐳 Job 2: Build & Push Docker Image (Continuous Deployment)*
```bash
.
├── C -->|Tests Pass ✅| D[🐳 Job 2: Build & Push Docker Image]
├── C -->|Tests Fail ❌| E[⛔ Pipeline Stops]
└── D --> F[📦 Docker Image Available on Docker Hub]
```

## 🔐 GitHub Secrets Required 🔑

<table style="width:100%; border-collapse: collapse; text-align: center; font-family: Arial, sans-serif;">
  <thead>
    <tr style="background-color:#0d1117; color:#ffffff;">
      <th style="padding:12px; border:1px solid #30363d;">🔑 Secret Name</th>
      <th style="padding:12px; border:1px solid #30363d;">📝 Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #30363d;"><strong>DOCKERHUB_USERNAME</strong></td>
      <td style="padding:10px; border:1px solid #30363d;">Docker Hub account username</td>
    </tr>
    <tr style="background-color:#161b22;">
      <td style="padding:10px; border:1px solid #30363d;"><strong>DOCKERHUB_TOKEN</strong></td>
      <td style="padding:10px; border:1px solid #30363d;">Docker Hub access token used for authentication</td>
    </tr>
  </tbody>
</table>
