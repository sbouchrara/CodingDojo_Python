from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create a route that responds with "Hi" and whatever name is in 
# the URL after /say/
@app.route('/say/<name>')
def say(name):
    return 'Hi '+ name.capitalize()+'!'

# Create a route that responds with the given word repeated 
# as many times as specified in the URL
@app.route('/repeat/<int:num>/<name>')
def repeat(num,name):
    return name*num

# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<str:name>')
def say(name):
    return 'Hi '+ name.capitalize()+'!'

# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, 
# and the 3rd element is a string
@app.route('/repeat/<int:num>/<str:name>')
def repeat(num,name):
    return name*num

if __name__ == "__main__":
    app.run(debug=True)
