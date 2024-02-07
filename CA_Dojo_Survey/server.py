from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/result')
def result():
    return render_template("result.html")


@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    print(request.form)
    session['name']     = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")



if __name__ == "__main__":
    app.run(debug=True)


