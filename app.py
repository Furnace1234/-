from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template("hello.html")

@app.route("/", methods=["GET", "POST"])
def start_view():
    return render_template("view.html")

@app.route("/1", methods=["GET", "POST"])
def start_228():
    return render_template("228.html")

@app.route("/2", methods=["GET", "POST"])
def start_111():
    return render_template("111.html")


@app.route("/reapp", methods=["GET", "POST"])
def reapp():
    return render_template("view.html")
    

app.run()