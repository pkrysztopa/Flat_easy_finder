from flask import render_template, redirect, url_for, Blueprint, request, session, flash ### 0

show_table = Blueprint("login", __name__)


@show_table.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.update({"nick" : request.form['nickname']})
        flash("You've been successfully logged in.") ### 1
    elif request.method == "GET" and "nick" not in session:
        return render_template("login.html")
    elif request.method == "GET" and "nick" in session: ### 2
        flash("Already logged in!") ### 2.1
    return redirect(url_for("dashboard.dashboard"))

