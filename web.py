from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__,static_url_path='')
rng = np.random.default_rng()

label=np.arange(1024)
value=np.zeros(1024)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]



@app.route("/")
def home():
    return render_template("giris.html")
@app.route("/graph")
def graph():
    
    return render_template("fullgraph.html",title='Graph I',  label=label.tolist(), value=value.tolist())


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

@app.route("/detectors/<int:numara>")
def dedektor(numara):
    return render_template("ornekdet.html",number=numara)



def load_data():
    print("çalıştı")
    for k in range(10000):
        i = round(np.random.normal(3,0.1)*100)
        value[i] = value[i]+1
        j = round(rng.normal(768,30))
        value[j] = value[j]+1
        z= round(rng.normal(600,20))
        value[z] = value[z]+1

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=load_data, trigger="interval", seconds=1)
    scheduler.start()
    app.run(debug=True)
