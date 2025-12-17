from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

trees = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/deforestasi")
def deforestasi():
    return render_template("deforestasi.html")

@app.route("/mulai-menanam")
def mulai_menanam():
    return render_template("mulai-menanam.html", trees=trees)

@app.route("/tanam", methods=["POST"])
def tanam():
    global trees
    trees.append(random.choice(["tree1.png", "tree2.png"]))
    return redirect(url_for("mulai_menanam"))

@app.route("/reset")
def reset():
    global trees
    trees = []
    return redirect(url_for("mulai_menanam"))

if __name__ == "__main__":
    app.run(debug=True)
