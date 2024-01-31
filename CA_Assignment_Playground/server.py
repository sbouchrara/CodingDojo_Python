from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:num>/<pcolor>')
def home_2(num,pcolor):
    return render_template("home.html",num=num,pcolor=pcolor)

@app.route('/play/<int:num>')
def home(num):
    return render_template("home.html",num=num,pcolor="blue")


@app.route('/play')
def home_1():
    return render_template("home.html",num=3,pcolor="blue")


if __name__=="__main__":
    app.run(debug=True)
