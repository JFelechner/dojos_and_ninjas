from flask_app import app
from flask import Flask,render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new_ninja_page')
def new_ninja_page():
    dojos = Dojo.get_all()
    return render_template("new_ninjas.html", dojos=dojos)



@app.route('/add_ninja', methods=["POST"])
def add_ninja():

    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    print(request.form)
    ninja = Ninja.save(data)
    print(ninja)
    return redirect('/')


