from flask import Flask, render_template, redirect, url_for, request, send_from_directory,Markup
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
from datetime import date




app = Flask(__name__,static_url_path='')
x = []
label=np.arange(1024)
value=np.zeros(1024)



@app.route("/")
def home():
    return render_template("giris.html")
@app.route("/graph")
def graph(): 
    return render_template("fullgraph.html",title='Graph I',  label=label.tolist(), value=value.tolist())
@app.route("/graph2")
def graph2():
    fig = px.bar(x=range(10), y=range(10))
    x  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [9, 6, 2, 1, 5, 4, 6, 8, 1, 3]
    y2 = [19, 36, 12, 1, 35, 4, 6, 8, 1, 3]
    trace1 = go.Bar(x=x,
                    y=y1,
                    name='Boats')
    trace2 = go.Bar(x=x,
                    y=y2,
                    name='Cars')

    data = [trace1, trace2]
    layout = go.Layout(title='Title',
                    xaxis=dict(title='X axis',
                                tickfont=dict(size=14,
                                                color='rgb(107, 107, 107)'),
                                tickangle=-45),
                    yaxis=dict(title='Y axis',
                                titlefont=dict(size=16,
                                                color='rgb(107, 107, 107)'),
                                tickfont=dict(size=14,
                                                color='rgb(107, 107, 107)')),)

    fig = go.Figure(data=trace1, layout=layout)
    plt_div2=plot(fig,
        include_plotlyjs='cdn',
        output_type='div')


    today = date.today()
    plt_div = plot(fig, output_type='div',filename=today.strftime("%b-%d-%Y"),image_filename=today.strftime("%b-%d-%Y"))
    p = Markup(plt_div2)
    
    return render_template("graph2.html",   plotlyfigure=p)


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
    for _ in range(10000):
        i = round(np.random.normal(3,0.1)*100)
        value[i] = value[i]+1


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=load_data, trigger="interval", seconds=5)

    scheduler.start()
    app.run(debug=True)
