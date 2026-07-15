# Vale's Unit Converter

A simple web-based unit converter built with Flask that supports conversions for Length, Weight, and Temperature units.

This project was created as part of my Python and Flask learning journey.

Project URL:
https://roadmap.sh/projects/task-tracker
---

## Features

### Length Conversion

- Millimeter
- Centimeter
- Meter
- Kilometer
- Inch
- Foot
- Yard
- Mile

### Weight Conversion

- Milligram
- Gram
- Kilogram
- Ounce
- Pound

### Temperature Conversion

- Celsius
- Fahrenheit
- Kelvin

Additional features include:

- User-friendly interface
- Input validation and error handling
- Accurate unit conversions
- Temperature unit symbols in the output

---

## Technologies Used

- Python 3
- Flask
- HTML
- CSS

---

## Project Structure

```text
vale-unit-converter/
│
├── app.py
│
├── templates/
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
│
├── static/
│   └── style.css
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/vale-unit-converter.git
```

Move into the project directory:

```bash
cd vale-unit-converter
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the Flask application:

```bash
flask run
```

or

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How It Works

### Length Conversion

All values are converted into meters before being converted to the selected unit.

```text
Kilometer
    ↓
 Meter
    ↓
Selected Unit
```

### Weight Conversion

All values are converted into grams before being converted to the selected unit.

```text
Kilogram
     ↓
   Gram
     ↓
Selected Unit
```

### Temperature Conversion

All values are converted into Celsius before being converted to the selected unit.

```text
Fahrenheit / Kelvin
          ↓
       Celsius
          ↓
    Selected Unit
```

---

## Error Handling

The application validates user input before performing conversions.

Example:

```text
abc
```

returns:

```text
Invalid input. Please enter a valid number.
```

---

## Future Improvements

Planned additions include:

- Area conversion
- Volume conversion
- Time conversion
- Improved UI/UX design
- Mobile responsiveness
- Unit testing

---

## Author

**Dzannun**

Built while learning Python, Flask, and web development.