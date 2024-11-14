from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Zhaoyang's Flask App!</h1><p>Try the /random route for a surprise.</p>"

@app.route("/random")
def random_number():
    return f"<h1>Here's a random number: {random.randint(1, 1000)}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
