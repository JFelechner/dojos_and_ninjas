from flask_app import app
from flask import Flask,render_template,redirect,request
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos=dojos)



@app.route('/add_dojo', methods=["POST"])
def add_dojo():

    data = {
        "name": request.form["name"],
    }
    dojo = Dojo.save(data)
    print(dojo)
    return redirect('/')



@app.route('/dojo/<int:id>')
def dojo_member_page(id):

    data={
        "id":id
    }

    dojos = Dojo.get_one(data)
    return render_template("dojo.html", dojos=dojos)

