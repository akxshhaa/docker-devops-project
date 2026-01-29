from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello! Automated Web App Deployment Project is running."

@app.route("/health")
def health():
    return {"status": "Application is running"}

if _name_ == "_main_":
    app.run(debug=True)