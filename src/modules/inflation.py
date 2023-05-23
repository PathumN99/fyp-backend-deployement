from flask import jsonify
import pymysql

class InflationClass:

    def inflation_getall(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='inflation_db'
            )
            cursor = conn.cursor()
            sql = "SELECT * FROM inflation"
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for result in results:
                user = {'id': result[0], 'date': result[1], 'rate': result[2]}
                users.append(user)

            return jsonify(users)

        except Exception as e:
            return jsonify({'error': str(e)})