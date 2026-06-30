from flask import Flask, render_template, request

app = Flask(__name__)

#Routes
@app.route('/')
def length():
    return render_template('length.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')