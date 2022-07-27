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

    #seating chart
    seatingChart = "PLACE HOLDER FOR SEATING CHART MATRIX"

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