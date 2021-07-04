#!/usr/bin/python3
# -*- coding: UTF-8
import os
import errno
import wget
import requests

print("Ingrese el DNI:")
dni = input()

BASE_URL = 'https://dniruc.apisperu.com/api/v1/dni/'+dni
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImhhY2tpbmdldGljbzIxQGdtYWlsLmNvbSJ9.swwgzb49yDH1QtzY9sShOA4jWnLgA_bhM9MHWPsRcBM"

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(BASE_URL, headers=headers)

datos = auth_response.json()
print("")
print("Dni: ")
print(datos['dni'])
print("Nombres: ")
print(datos['nombres'])
print("Apellido Paterno: ")
print(datos['apellidoPaterno'])
print("Apellido Materno: ")
print(datos['apellidoMaterno'])
print("") 

try:
    os.mkdir('c'+dni)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
os.chdir('c'+dni)

url = "http://www.enlacesframework.info/vfpsapirenic/images/foto/"+dni+".jpg"
wget.download(url, './')
print(" La foto del el dni " +dni+ " fue guardada en la carpeta principal")
print("")
url = "http://www.enlacesframework.info/vfpsapirenic/images/firma/"+dni+".jpg"
wget.download(url, './')
print(" La foto de la firma fue guardada")
print("")
url = "http://www.enlacesframework.info/vfpsapirenic/images/huellas/i"+dni+".jpg"
wget.download(url, './')
print(" Huella Izquierda descargada")
print("")
url = "http://www.enlacesframework.info/vfpsapirenic/images/huellas/d"+dni+".jpg"
wget.download(url, './')
print(" Huella Derecha descargada")
print("")
print("Módulo Finalizado")
