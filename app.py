from flask import Flask,render_template,request
import time
from threading import Thread
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

takim = ""
gs_count=0
fb_count=0
bjk_count=0
@app.route("/takim",methods=['POST'])
def takim():
    global takim
    global gs_count
    global fb_count
    global bjk_count
    if request.method == 'POST':
        if request.form['submit_button']== "Galatasaray":
            takim = "gs"
            gs_count +=1
            return render_template("index.html",flag="posted")
        elif request.form['submit_button']=="Fenerbahce":
            takim = "fb"
            fb_count +=1
            return render_template("index.html",flag="posted")
        elif request.form['submit_button']=="Besiktas":
            takim = "bjk"
            bjk_count+=1
            return render_template("index.html",flag="posted")

@app.route("/sound",methods=['GET'])
def play_sound():
    global takim
    if(takim=="gs"):
        takim = ""  
        return render_template("playsound.html",value="gs")
    elif (takim == "bjk"):
        takim = ""
        return render_template("playsound.html", value ="bjk")
    elif (takim == "fb"):
        takim = ""
        return render_template("playsound.html",value = "fb",)
    else:
        return render_template("playsound.html",gs = gs_count, fb = fb_count,bjk =bjk_count)
if __name__ == "__main__":
    app.run(debug=True,host="192.168.1.49")