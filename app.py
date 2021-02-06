from flask import Flask, request, render_template, redirect, url_for
import joblib
import numpy as np
import pprint
# Logging IS REMAINING

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")
    # CHANGE THE NAME OF INDEX TO IRIS.HTML
    # SINCE IT WONT BE OUR HOMEPAGE
    # ADDING A NAV BAR IN  (half done)✌✌✌
    # MAKING MY OWN PERSONAL BIO WEBSITE ON
    # HEROKU


@app.route("/test")
def testing():
    '''
    since nav bar is already in the base temp
    we do not use extends or anything fancy
    '''
    return render_template('Testing the site ✌✌✌')


@app.route('/result', methods=['POST'])
def result():
    '''
    when the submit button is pressed
    '''
    sepal_len = float(request.form['sepal length'])
    sepal_width = float(request.form['sepal width'])
    petal_len = float(request.form['petal length'])
    petal_width = float(request.form['petal width'])
    values.extend([sepal_len, sepal_width, petal_len, petal_width])
    preds = str(model.predict([values]))
    values.clear()
    return render_template('result.html', type=preds)
# Handling Error


@app.errorhandler(ValueError)
def error(arg):
    return render_template('ValueError.html')


@app.errorhandler(Exception)
def error(arg):
    ''' 
    no. of vars declared in the html should be filled in the fn
    and arguments of same numbers should also be given in
    in the fn error(arg)
    '''
    return render_template('error.html', var=arg)


# ADDING BG
if __name__ == '__main__':
    values = []
    file = open('iris.pkl', 'rb')
    model = joblib.load(file)
    app.run(debug=True)


# <form method = "post" action = "/" >
# <button type = "submit" name = "submit_a" value = "submit_a" > Submit_a < /button >
# <button type = "submit" name = "submit_b" value = "submit_b" > Submit_b < /button >
# </form >


# def submit():
# 	if request.method == "POST":
# 		if request.form.get("submit_a"):
# 			# do something
# 		elif request.form.get("submit_b"):
# 			# do something else
# 	elif request.method == "GET":
# 		# do something
