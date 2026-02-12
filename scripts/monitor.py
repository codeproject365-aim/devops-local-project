import subprocess

def check_containers():
    print("📊 Checking Running Containers...")
    subprocess.run(["docker", "ps"])

if __name__ == "__main__":
    check_containers()
