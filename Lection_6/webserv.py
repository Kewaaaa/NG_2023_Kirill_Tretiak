from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from dbworker import *



app = Flask("news")



@app.route("/")
def index():
    result = read_news()
    return render_template("index.html", result = result)

@app.route("/verification", methods = ["POST", "GET"])
def ver():
    if request.method == "POST":
        verify = verification(request.form.get("username"))
        if verify is None:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('admin', username = verify[0]))

@app.route("/admin/<username>", methods = ["POST", "GET"])
def admin(username):
    time = date.today()
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        add_news(username, title, content, time)
    result = read_news()
    return render_template("admin.html", username = username, time = time, result = result)

app.run(host="0.0.0.0", port="8081")
