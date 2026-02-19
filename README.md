 🚀 DevOps Multi-Container Application

This is a simple DevOps project demonstrating a multi-container setup using Docker and Docker Compose.  
The project runs a frontend and backend service in separate containers.

 📌 Project Description

This project shows how to:

- Run multiple services using Docker Compose
- Connect frontend and backend containers
- Expose services on different ports
- Manage a basic DevOps project structure
- Push and manage code using GitHub

🛠 Technologies Used

- 🐳 Docker
- 🐳 Docker Compose
- ⚙️ Node.js (Backend)
- 🌐 HTML / CSS / JavaScript (Frontend)
- 🗂 Git & GitHub

 📂 Project Structure

 project-root/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── docker/
│   └── Dockerfile
│
├── docker-compose.yml
├── Jenkinsfile
└── README.md

 🛠️ Setup Instructions (Local)

1. Clone the repository

   git clone https://github.com/your-username/your-repo-name.git

2. Navigate into project directory

   cd your-repo-name

3. Build and start containers

   docker compose up --build

4. Access application

   http://localhost:5000

 ☁️ Deployment Steps 

- Launch EC2 instance (Ubuntu)
- Install Docker and Docker Compose
- Clone repository
- Run docker compose up -d
- Configure Nginx reverse proxy
- Access using EC2 public IP

  📖 Learning Outcome

- Understanding of containerization
- CI/CD automation workflow
- Cloud deployment process
- Reverse proxy configuration
- Basic DevOps best practices

👨‍💻 Author
Sanskar Rajput  

