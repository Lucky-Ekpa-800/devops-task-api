from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "DevOps Task API is running!"


@app.route("/health")
def health():
    return {"status": "healthy"}


tasks = [
    {
        "id": 1,
        "task": "Learn Docker and Kubernetes",
        "completed": False
    },
    {
        "id": 2,
        "task": "Deploy to Azure with Terraform",
        "completed": False
    }
]


@app.route("/tasks")
def get_tasks():
    return tasks


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)