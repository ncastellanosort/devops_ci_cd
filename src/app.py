from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Hello DevOps, this is a full cicle explaination (CI/CD). Now with Flux for GitOps"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
