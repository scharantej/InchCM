
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=["POST"])
def calculate():
    inches = float(request.form.get('inches'))
    centimeters = inches * 2.54
    return redirect(url_for('results', centimeters=centimeters))

@app.route('/results')
def results():
    centimeters = request.args.get('centimeters')
    return render_template('results.html', centimeters=centimeters)

if __name__ == '__main__':
    app.run(debug=True)
