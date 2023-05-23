from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS
from src.modules.analysis import AnalysisClass
from src.modules.inflation import InflationClass
from src.modules.cpi import CpiClass

app = Flask(__name__)
CORS(app)

# Create a connection to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='inflation_db'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

analysisClass = AnalysisClass()
inflationClass = InflationClass()
cpiClass = CpiClass()


# GET all analysis data
@app.route('/analysis/get-all', methods=['GET'])
def get_all_analysis():
    try:
        records = analysisClass.analysis_getall()
        return records
    except Exception as e:
        return jsonify({'error': str(e)})


# Create an analysis
@app.route('/analysis/create', methods=['POST'])
def create_item():
    try:
        date = request.json['date']
        description = request.json['description']
        createRecord = analysisClass.create_analysis(date, description)
        return createRecord

    except Exception as e:
        return jsonify({'error': str(e)})


# GET all inflation data
@app.route('/inflation/get-all', methods=['GET'])
def get_all_inflation():
    try:
        records = inflationClass.inflation_getall()
        return records
    except Exception as e:
        return jsonify({'error': str(e)})


# GET all cpi data
@app.route('/cpi/get-all', methods=['GET'])
def get_all_cpi():
    try:
        cpi_records = cpiClass.cpi_getall()
        return cpi_records
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)