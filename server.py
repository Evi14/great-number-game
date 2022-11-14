from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'gfhjmbjkvgdsfvds'
attempts = 0
randomNum = random.randint(1, 100) 		# random number between 1-100
@app.route('/')
def index():
    print(randomNum)
    return render_template("index.html", randomNum = randomNum, attempts= attempts)    

@app.route("/lose")
def game_over():
    return render_template("gameOver.html", attempts= attempts)

@app.route("/guessing", methods=["POST"])
def find_num():
    global attempts
    if attempts<4:
        session['number'] = (int(request.form['numberguess']))
    else:
        attempts += 1
        return redirect("/lose")
    attempts += 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset_session():
    return redirect("/destroy_session")

@app.route("/destroy_session")
def destroy():
    session.clear()
    global attempts
    attempts = 0
    global randomNum
    randomNum = random.randint(1, 100)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
