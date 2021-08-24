from flask import Flask
from flask import render_template, request
#from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/classes", methods = ['POST', 'GET'])
def classes():
    courses = {
        'CS111' : ['Introduction to Algorithmic Problem-Solving', 'A', '5'],
        'CS112' : ['Introduction to Algorithmic Problem-Solving in Java', 'A', '5'],
        'CS120' : ['Discrete Mathematics' 'B', '10'],
        'CS211' : ['Object-Oriented Programming in C++', 'B', '10'],
        'CS212' : ['Object-Oriented Programming in Java', 'B', '10'],
        'CS220' : ['Discrete Structures', 'C', '15'],
        'CS240' : ['Computer Organization and Assembly Language', 'B', '10'],
        'CS313' : ['Data Structures', 'C', '15'],
        'CS316' : ['Principles of Programming Languages', 'B', '10'],
        'CS320' : ['Theory of Computation', 'B', '10'],
        'CS323' : ['Design and Analysis of Algorithms', 'C', '15'],
        'CS331' : ['Database Systems', 'B', '10'],
        'CS334' : ['Data Mining and Warehousing', 'B', '10'],
        'CS340' : ['Operating Systems Principles', 'C', '15'],
        'CS343' : ['Computer Architecture', 'C', '15']
    }
    if request.method == "POST":
        courseDistribution(request.form)
    return render_template("classes.html", courses = courses)



def courseDistribution():




