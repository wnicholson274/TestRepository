from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import BMIForm, BMRForm
from BMICalc import BmiCalc
from BMRCalc import BmrCalc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    form = BMIForm()
    bmi_result = None
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        unit = form.unit.data

        bmi_result = BmiCalc(weight, height, unit)

    return render_template('bmi.html', form=form, bmi_result=bmi_result)

@app.route('/bmr', methods=['GET', 'POST'])
def bmr():
    form = BMRForm()
    bmr_result = None
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        age = form.age.data
        gender = form.gender.data
        unit = form.unit.data

        bmr_result = BmrCalc(unit, weight, height, age, gender)

    return render_template('bmr.html', form=form, bmr_result=bmr_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
