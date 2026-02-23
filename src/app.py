from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Hello DevOps, this is a full cicle explaination (CI/CD)."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
