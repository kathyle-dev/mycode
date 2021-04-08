#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
from groups import group_list

app = Flask(__name__)
app.secret_key = "IT'S A SECRET"


## If the user hits the root of our API
@app.route("/", methods=["POST", "GET"])
def index():
    ## if the key "username" has a value in session
    if request.method == "GET":
        if "username" not in session:
            return "You are not logged in!" + "<br>" + \
                   "<b><a href = '/login'>click here to log in</a></b>"

    if request.method == "POST":
        new_group = {
            "hostname": request.form.get("hostname"),
            "ip": request.form.get("ip"),
            "fqdn": request.form.get("fqdn")
        }
        group_list.append(new_group)

    return render_template("hosts.html", qparams=group_list)


@app.route("/add")
def addAPost():
    return """
                <h2>add group information</h2>
                <form action ="/" method = "post">
                <p><input type = text placeholder="Hostname" name = hostname></p>
                <p><input type = text placeholder="IP" name = ip></p>
                <p><input type = text placeholder="FQDN" name = fqdn></p>
                <p><input type = submit >Submit</p>
                </form>
                """


## If the user hits /login with a GET or POST
@app.route("/login", methods=["POST", "GET"])
def login():
    ## if you sent us a POST because you clicked the login button
    if request.method == "POST":
        ## request.form["xyzkey"]: use indexing if you know the key exists
        ## request.form.get("xyzkey"): use get if the key might not exist
        session["username"] = request.form.get("username")
        if session["username"] == "admin":
            return redirect(url_for("addAPost"))
    else:
        ## return this HTML data if you send us a GET
        return """
        <h2>Log in:</h2>
       <form action = "/login" method = "post">
          <p><input type = text name = username></p>
          <p><input type = submit value = Login></p>
       </form>
      """


@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
