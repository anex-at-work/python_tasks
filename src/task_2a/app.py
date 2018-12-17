from flask import Flask, jsonify, request, Response
from requests import RequestCheck
from calculator import Calculator


app = Flask(__name__)


@app.route('/calc', methods=['POST'])
def calc():
    req = RequestCheck(request)
    if not req.is_correct():
        return jsonify(req.errors), 400
    calc = Calculator(req.expression)
    res = calc.simple_calc() if req.simplify else calc.calc()
    if res is None:
        return jsonify(calc.errors), 400
    return jsonify({'result': res})

