from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

TREE_IMAGES = ["tree1.png", "tree2.png"]

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
    trees.append(random.choice(TREE_IMAGES))
    return redirect(url_for("mulai_menanam"))

@app.route("/reset")
def reset():
    trees.clear()
    return redirect(url_for("mulai_menanam"))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = None
    if request.method == "POST":
        answers = {
            "q1": "b",
            "q2": "a",
            "q3": "c",
            "q4": "a",
            "q5": "a",
            "q6": "b",
        }
        score = 0
        for q, correct in answers.items():
            if request.form.get(q) == correct:
                score += 1

    return render_template("quiz.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)