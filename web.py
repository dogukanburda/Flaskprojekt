from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("giris.html")
@app.route("/graph")
def graph():
    return render_template("fullgraph.html")


@app.route("/admin")
def admin():
	return redirect(url_for("home"))

@app.route("/login", methods= ["POST","GET"])
def login():
    if request.method == "POST":
        number = request.form["number"]
        return redirect(url_for("dedektor", numara=number))
    else:
        return render_template("detinput.html")

@app.route("/detectors/<numara>")
def dedektor(numara):
    return render_template("ornekdet.html",number=numara)





if __name__ == "__main__":
    app.run(debug=True)