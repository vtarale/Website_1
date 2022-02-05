from flask import Flask, render_template, request

app = Flask(__name__)

accounts = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register1", methods=["GET"])
def go_to_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form.get("password") != request.form.get("repassword"):
        return render_template("fail.html")
    if request.form.get("account") not in list(accounts):
        accounts[request.form.get("account")] = [request.form.get("password")]
        return render_template("success.html")
    return render_template("fail.html")

@app.route("/people", methods=["GET"])
def people():
    return render_template("people.html", registered=list(accounts))

@app.route("/deregister1", methods=["POST"])
def go_to_deregister():
    return render_template("deregister.html")

@app.route("/deregister", methods=["POST"])
def deregister():
    if request.form.get("account") not in list(accounts):
        return render_template("fail.html")
    if [request.form.get("password")] != accounts[request.form.get("account")]:
        return render_template("fail.html")
    del accounts[request.form.get("account")]
    return render_template("success.html")
