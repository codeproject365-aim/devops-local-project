import subprocess

def build_images():
    print("🔨 Building Docker Images...")
    subprocess.run(["docker-compose", "build"])

def deploy_services():
    print("🚀 Deploying Services...")
    subprocess.run(["docker-compose", "up", "-d"])

def health_check():
    print("🩺 Checking Backend Health...")
    subprocess.run(["curl", "http://localhost:5000/health"])

if __name__ == "__main__":
    build_images()
    deploy_services()
    health_check()
