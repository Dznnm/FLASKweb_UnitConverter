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
    to_unit = ""
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
        except ValueError:
            result = "Invalid input. Please enter a valid number."
            return render_template('length.html', result=result, to_unit=to_unit)

        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        base = value * length_units[from_unit]
        result = round(base / length_units[to_unit],2)
    return render_template('length.html', result=result, to_unit=to_unit)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = "Enter a value and select units to convert."
    to_unit = ""
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
        except ValueError:
            result = "Invalid input. Please enter a valid number."
            return render_template('weight.html', result=result, to_unit=to_unit)

        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        base = value * weight_units[from_unit]
        result = round(base / weight_units[to_unit],2)
    return render_template('weight.html', result=result, to_unit=to_unit)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = "Enter a value and select units to convert."
    to_unit = ""
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
        except ValueError:
            result = "Invalid input. Please enter a valid number."
            return render_template('temperature.html', result=result, unit_symbol=to_unit)
        
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        if from_unit == 'celsius':
            base = value
        elif from_unit == 'fahrenheit':
            base = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            base = value - 273.15

        if to_unit == 'fahrenheit':
            result = round((base * 9/5) + 32, 2)
        elif to_unit == 'celsius':
            result = round(base, 2)
        elif to_unit == 'kelvin':
            result = round(base + 273.15, 2)

        if to_unit == 'fahrenheit':
            unit_symbol = '°F'
        elif to_unit == 'celsius':
            unit_symbol = '°C'
        elif to_unit == 'kelvin':
            unit_symbol = 'K'
    return render_template('temperature.html', result=result, unit_symbol=unit_symbol)