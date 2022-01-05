from flask import Flask, render_template, request, flash

app = Flask(__name__) #creating a class
app.secret_key = "password"

@app.route("/hello") #last part of the url
def index(): #assiociating the route with a function
    flash("what's your name?")
    return render_template("index.html") #were choosing a template from the templates folder

@app.route("/greet", methods=["POST", "GET"]) #routing to the button press
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")