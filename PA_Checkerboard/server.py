from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/play')
@app.route('/')
def home_1():
    return render_template("home.html",numtr=8,numtd=8,pcolor1="black",pcolor2="red")

@app.route('/<int:numtr>')
def home_2(numtr):
    return render_template("home.html",numtr=numtr,numtd=8,pcolor1="black",pcolor2="red")

@app.route('/<int:numtr>/<int:numtd>')
def home_3(numtr,numtd):
    return render_template("home.html",numtr=numtr,numtd=numtd,pcolor1="black",pcolor2="red")

@app.route('/<int:numtr>/<int:numtd>/<pcolor1>')
def home_4(numtr,numtd,pcolor1):
    return render_template("home.html",numtr=numtr,numtd=numtd,pcolor1=pcolor1,pcolor2="red")

@app.route('/<int:numtr>/<int:numtd>/<pcolor1>/<pcolor2>')
def home(numtr,numtd,pcolor1,pcolor2):
    return render_template("home.html",numtr=numtr,numtd=numtd,pcolor1=pcolor1,pcolor2=pcolor2)

if __name__=="__main__":
    app.run(debug=True)