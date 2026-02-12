from flask import Flask, jsonify
import socket
import os
import psycopg2
import time

app = Flask(__name__)

def check_db_connection():
    try:
        conn = psycopg2.connect(
            host="db",
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        conn.close()
        return "Connected"
    except:
        return "Not Connected"

@app.route("/")
def home():
    return "DevOps Backend Running 🚀"

@app.route("/health")
def health():
    hostname = socket.gethostname()
    db_status = check_db_connection()

    return jsonify({
        "status": "healthy",
        "hostname": hostname,
        "database": db_status
    })

if __name__ == "__main__":
    time.sleep(5)  # wait for DB
    app.run(host="0.0.0.0", port=5000)
