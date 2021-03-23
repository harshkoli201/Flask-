from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello This is my First web page <h1> Flask Web Page </h1>"

if __name__ == "__main__":
    app.run(debug=True)