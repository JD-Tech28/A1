from flask import Flask, render_template, request
import random 

app = Flask(__name__)

number = random.randint(1,100)
total = 0 

@app.route("/", methods=["Get", "post"])
def home():
    global total
    message =""

    if request.method =="post":
        guess= int(request.form["Guess"])
        total +=1

        if guess == number:
            message = f"correct! Attempts: {total}"
        elif guess < number:
            message = "Up"
        else:
            message= "down"
    return render_template("index.html", message=message)

if __name__=="__main__":
    app.run(debug=True)