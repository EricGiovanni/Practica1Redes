import os
import requests

from flask import Flask
from flask import request
from flask.json import jsonify

from decouple import config
from getmac import get_mac_address as gma

app = Flask(__name__)

URL = config("RUTA1", cast=str)
URL2 = config("RUTA2", cast=str)
mac = gma()
name = "Eric"


@app.route("/", methods=["POST"])
def ciclo():
    request_data = request.get_json()
    print("Ahora tengo el valor: " + str(request_data['valor']))
    print("Enviando a la siguiente URL..." + URL)
    mensaje = "El ciclo ha comenzado"
    if(request_data['valor'] < 50):
        requests.post(
            URL, json={"valor": request_data['valor'] + 1, "mac": mac, "name": name})
    else:
        print("He finalizado")
        requests.post(
            URL + "/finish", json={"valor": request_data['valor'], "mac": mac, "name": name})
        requests.post(
            URL2 + "/finish", json={"valor": request_data['valor'], "mac": mac, "name": name})
    return jsonify({"message": mensaje, "statusCode": 200, "mac": mac, "name": name})


@app.route("/finish", methods=["POST"])
def finish():
    request_data = request.get_json()
    finish_valor = request_data['valor']
    finish_mac = request_data['mac']
    finish_name = request_data['name']
    print("El ciclo ha terminado con el valor: " + str(finish_valor))
    print("La mac de quien termino el ciclo es: " + str(finish_mac))
    print("El nombrde de quien termino el ciclo es: " + str(finish_name))
    return jsonify({"message": "El ciclo ha terminado", "statusCode": 200})


@app.route("/get-ram", methods=["GET"])
def get_ram():
    ram_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    ram_gigabytes = ram_bytes / (1024**3)
    return jsonify({"message": "La cantidad de memoria ram aparecerá a continuación", "statusCode": 200, "ram": ram_gigabytes})


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
