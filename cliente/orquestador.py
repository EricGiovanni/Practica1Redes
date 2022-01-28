import os
import requests

from typing import cast

from decouple import config

from getmac import get_mac_address as gma

URL = config("LOCALHOST", cast=str)
URL1 = config("RUTA1", cast=str)
URL2 = config("RUTA2", cast=str)


def get_mayor_ram_and_send():
    ram1 = (os.sysconf("SC_PAGE_SIZE") *
            os.sysconf("SC_PHYS_PAGES")) / (1024**3)
    ram2 = requests.get(URL1 + "/get-ram").json()['ram']
    ram3 = requests.get(URL2 + "/get-ram").json()['ram']
    mac = gma()
    response = ""
    if(ram1 >= ram2 and ram1 >= ram3):
        response = requests.post(
            URL, json={"valor": 0, "mac": mac, "name": "Eric"})
    elif(ram2 > ram1 and ram2 > ram3):
        response = requests.post(
            URL1, json={"valor": 0, "mac": mac, "name": "Eric"})
    else:
        response = requests.post(
            URL2, json={"valor": 0, "mac": mac, "name": "Eric"})
    print(response.json())


get_mayor_ram_and_send()
