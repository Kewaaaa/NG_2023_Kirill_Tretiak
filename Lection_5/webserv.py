from flask import Flask, render_template, request, redirect, url_for

app = Flask("app1")

user = {}
messages = []

@app.route("/", methods = ["POST", "GET"])
def main():
    if request.form.get("login"):
        return redirect(url_for('login'))
    elif request.form.get("signin"):
        return redirect(url_for('signin'))
    return render_template("main.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if not request.form.get('username') or not request.form.get('password'):
        return render_template("login.html")
    else:
        user[request.form.get('username')] =request.form.get('password')
        return redirect(url_for('chat', username=request.form.get('username')))
    
@app.route("/signin", methods = ["POST", "GET"])
def signin():
    if request.form.get('username') in user and user[request.form.get('username')] == request.form.get('password'):
        return redirect(url_for('chat', username=request.form.get('username')))
    return render_template("signin.html")

@app.route("/profile/<username>/chat", methods = ["POST", "GET"])
def chat(username):
    if request.method == "POST":
        messages.append(username)
        messages.append(request.form.get('msg'))
    return render_template("chat.html", message=messages, username=username)


app.run(host="0.0.0.0", port="8081")