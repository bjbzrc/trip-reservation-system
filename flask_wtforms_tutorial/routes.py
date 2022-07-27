from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .forms import *
import numpy


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    #check if the request method is POST. POST method means that form data was submitted
    #So, if method is POST we can get the form data 
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            #if form option is "1" go to the admin page
            return redirect('/admin')
        else:
            #if form option is "2" go to the reservations page
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")


@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    #get valid admin users
    validUser = []
    validPw = []
    try:
        with open("passcodes.txt") as fp:
            lines = fp.read().splitlines()
        for line in lines:
            users = line.split(',')
            validUser.append(users[0])
            validPw.append(users[1].lstrip())
    except Exception as e:
        print(e)

    #get seating placement
    reservedSeats = []
    try:
        with open("reservations.txt") as fp:
            lines = fp.read().splitlines()
        for line in lines:
            seat = line.split(',')
            x = int(seat[1])
            y = int(seat[2])
            reservedSeats.append([x, y])
    except Exception as e:
        print(e)

    #calculate cost
    #seat prices
    totalPrices = 0
    costMatrix = [[100, 75, 50, 100] for row in range(12)]
    for seat in reservedSeats:
        totalPrices +=  costMatrix[seat[0]][seat[1]]

    seatingChart = [['O'] * 4 for row in range(12)]
    for seat in reservedSeats:
        seat1 = int(seat[0])
        seat2 = int(seat[1])
        seatingChart[seat1][seat2] = 'X'

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in validUser:
            userIndex = validUser.index(username)
            if validPw[userIndex] == password:
                flash(f"Total Sales: {totalPrices}")
                return redirect(url_for("admin"))
        else:
            flash("Username or Password is incorrect.")
            return redirect(url_for("admin"))

    return render_template("admin.html", form=form, seatingChart=seatingChart, template="form-template")


@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

