from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't put on git"
    app.run(host="0.0.0.0", port=8700)
