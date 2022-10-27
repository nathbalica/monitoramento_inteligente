# import sys
# sys.path.append('../')
from postgres_connector.connect import Connect
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "API - Desafio monitoramento"


def serializer(tupla):

    result = {
        'id': tupla[0],
        'mac_name': tupla[1],
        'date': datetime.strftime(tupla[2], "%Y-%m-%dT%H:%M:%SZ"),
        'rssi': tupla[3],
        'va': tupla[4],
        'vb': tupla[5],
        'vc': tupla[6],
        'ia': tupla[7],
        'ib': tupla[8],
        'ic': tupla[9],
        'wa': tupla[10],
        'wb': tupla[11],
        'wc': tupla[12],
    }
    return result


@app.route('/get', methods=['GET'])
def result():
    
    cnx = Connect("postgres_atmos", "atmos_db", "atmos", "atmos", 5432)

    content = request.get_json()
    
    query = f"select * from measurer_data where mac_name = '{content['mac_adress']}' \
                    and date_measurer between '{content['date_inicial']}' and '{content['date_final']}'\
                    order by date_measurer asc;"
    
    result = cnx.select(query)
    
    data_result = [serializer(i) for i in result]
    
    return data_result

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)