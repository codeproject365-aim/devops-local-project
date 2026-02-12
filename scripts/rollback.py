import subprocess

def rollback_backend():
    print("⚠ Rolling Back Backend...")
    subprocess.run(["docker", "restart", "backend_service"])
    print("✅ Rollback Complete!")

if __name__ == "__main__":
    rollback_backend()
