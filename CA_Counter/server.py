from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')
def home():
    if "count" not in session:
        session["count"]=0
    else:
        session['count'] += 1
    return render_template("home.html")

@app.route('/reset')
def reset():
    session.clear()
    # print(session['counter_clic'])
    return redirect('/')

@app.route('/increment')
def increment():
    session['count'] += 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

