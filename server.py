
from flask import Flask, jsonify, request
from flask_cors import *
from get_predict_result import predict_for_datapoint

from process_data import make_people, pre_precess_for_model
from query_function import query_for_one_record
from upload_one_datapoint import upload_fun
import pandas as pd


app = Flask(__name__, static_url_path='')
CORS(app, supports_credentials=True)


@app.route('/')
@app.route('/patient', methods=['GET', 'POST'])
def predict():
    print("Hello!")
    data = request.get_json()
    dp = pd.DataFrame({k: [v] for k, v in data.items()})
    result = predict_for_datapoint(dp)
    print(f'The result is {result}.')
    json_back = {'answer': result}
    return jsonify(json_back)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print("Hello, Doctor!")
    data = request.get_json()
    dp = pd.DataFrame({k: [v] for k, v in data.items()})
    dp = dp.rename(columns={"test_result": "covid19_Res"})
    dp = pre_precess_for_model(dp)
    dp = dp.values.tolist()
    print(dp)
    dp = make_people(dp[0])
    num, pw = upload_fun(dp)
    print(f'current records number: {num}')
    json_back = {'answer': num,
                 'password': pw}
    return jsonify(json_back)


@app.route('/query', methods=['GET', 'POST'])
def query():
    print("Query!")
    data = request.get_data().decode()
    data = int(data)
    print(data)
    print(type(data))
    result = query_for_one_record(data)
    json = {'answer': result}
    return jsonify(json)


if __name__ == '__main__':
    app.run()
