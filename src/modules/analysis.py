from flask import jsonify
import pymysql


class AnalysisClass:

    def analysis_getall(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='inflation_db'
            )
            cursor = conn.cursor()
            sql = "SELECT * FROM analysis"
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for result in results:
                user = {'id': result[0], 'date': result[1], 'description': result[2]}
                users.append(user)

            return jsonify(users)

        except Exception as e:
            return jsonify({'error': str(e)})

    def create_analysis(self, date, description):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='inflation_db'
            )
            cursor = conn.cursor()
            sql = "INSERT INTO analysis (date, description) VALUES (%s, %s)"
            cursor.execute(sql, (date, description))
            conn.commit()

            return jsonify({'date': date, 'description': description})

        except Exception as e:
            return jsonify({'error': str(e)})