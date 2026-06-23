from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AutoMoneyMachine</h1>
    <h3>Website is Running Successfully!</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
