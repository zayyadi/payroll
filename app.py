from decimal import Decimal
from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS
from .pay import Grade

app = Flask(__name__)

cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/payslip', methods=['GET', 'POST'])
def payslip():
    name = request.form['name']
    gross = int(request.form['gross'])
    grade = Grade(name=name, gross=gross)
    monthly_pay = grade.get_net_pay_monthly()
    payee = grade.payee_logic() / 12
    cons = grade.get_consolidated_relief()
    taxable = grade.get_taxable_income()
    pension = grade.get_total_pension()
    response = jsonify({
        'payslip': monthly_pay,
        'payee': payee,
        'cons': cons,
        'taxable': taxable,
        'pension': pension/12,
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True)
