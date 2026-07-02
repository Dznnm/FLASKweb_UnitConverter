from flask import Flask, render_template, request

app = Flask(__name__)

#Conversions
length_units = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}
weight_units = {
    'milligram': 0.001,
    'gram': 1,
    'kilogram': 1000,
    'ounce': 28.3495,
    'pound': 453.592,
}

#Routes
@app.route('/', methods=['GET', 'POST'])
def length():
    result = "Enter a value and select units to convert."
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        base = value * length_units[from_unit]
        result = round(base / length_units[to_unit],2), to_unit
    return render_template('length.html', result=result, to_unit=to_unit)

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')