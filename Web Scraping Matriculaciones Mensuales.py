#!/usr/bin/env python
# coding: utf-8

# Inspeccionamos la página, y comprobamos que los datos se encuentran en un iframe.
# A través de la librería Selenium, podemos acceder a dicho iframe desde la URL original.

# Cargamos librerías necesarias.
from bs4 import BeautifulSoup
from selenium import webdriver

# Almacenamos la URL original.
url = "https://www.faconauto.com/matriculaciones-mensuales-turismos/"

# Abrimos un webdriver en el navegador Firefox.
# NOTA: Es necesario descargar el ejecutable Geckodriver, a través de: https://github.com/mozilla/geckodriver/releases,
# e incluirlo en el PATH donde se encuentre el código.
driver1 = webdriver.Firefox()

# Obtenemos la URL a través del driver.
driver1.get(url)

# Encontramos el iframe, clickamos sobre él, y nos cambiamos al directorio correspondiente.
iframeElement = driver1.find_element_by_tag_name("iframe")
iframeElement.click()
driver1.switch_to.frame(iframeElement)

# Creamos un objeto soup a través del driver, una vez nos hemos cambiado de directorio.
soup = BeautifulSoup(driver1.page_source, "html.parser")

# Imprimimos soup.prettify para estudiar la estructura de la URL del infograma.
print("Estructura HTML del infograma:", "\n")
print(soup.prettify, "\n")

'''
# En este bloque, se ofrece un modo alternativo de obtener el objeto soup, parseando directamente la URL del iframe (src).
# Cabe destacar que este método es menos flexible ante posibles cambios en el parámetro src.

import requests

# A través del parámetro "src", podemos acceder al enlace en el que se encuentran estos datos.
# Este será el enlace que usaremos para el web scraping.
page = requests.get("https://e.infogram.com/580ba5d8-99b4-4262-86ae-e335e3a02a5b?parent_url=https%3A%2F%2Fwww.faconauto.com%2Fmatriculaciones-mensuales-turismos%2F&amp;src=embed#async_embed")
print("Código de respuesta HTTP:", page)

# Almacenamos el objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Imprimimos soup.prettify para estudiar la estructura de la URL
print("Estructura HTML del infograma:", "\n")
print(soup.prettify, "\n")
'''

# Los números deseados se encuentran almacenados en un tag <script>.
# Procedemos a guardar todos estos tags en una nueva variable.
scripts_tags = soup.find_all("script")

# Imprimimos la nueva variable para comprobar donde están los datos deseados.
print("Los tags <script> en la página, son los siguientes:", "\n")
print(scripts_tags)

# Como los números se encuentran en el quinto tag <script>, lo almacenamos en una nueva variable,
# indexando el quinto valor de scripts_tags.
data_script = scripts_tags[5]
print("El script de destino es el siguiente", "\n")
print(data_script, "\n")

'''
# En caso de seleccionar la opción sin Selenium, será necesario acceder al 4o tag script.
data_script = scripts_tags[4]
print("El script de destino es el siguiente", "\n")
print(data_script)
'''

# Importamos la libreria re para poder encontrar la ubicación de los datos.
import re

# Transformamos el script almacenado al tipo de variable string.
data_script = str(data_script)

# Inspeccionando el script, vemos que la segunda aparición de "ENERO" da inicio a nuestros datos.
# A través de re.finditer, estudiamos
print("Los índices en los que encontramos el string 'ENERO', son:", "\n")
for match in re.finditer("ENERO", data_script):
    print (match.start(), match.end())
print("\n")
    
# En base al segundo valor, sabemos que podremos encontrar la lista completa del mes
# con la siguiente indexación:
print("Datos relativos a ENERO:", "\n")
print(data_script[22281:22315], "\n")

# Repetimos el proceso con el mes de diciembre, para saber en qué índice se encuentran 
# los últimos datos a extraer para nuestro dataset
print("Los índices en los que encontramos el string 'DICIEMBRE', son:", "\n")
for match in re.finditer("DICIEMBRE", data_script):
    print (match.start(), match.end())
print("\n")

# Para saber en qué punto finaliza el dataset, creamos una nueva variable desde el
# inicio del string "DICIEMBRE" de interés, y buscamos luego la primera aparición
# del carácter "]", que delimita el final de la lista.
diciembre = data_script[22655:]
diciembre.find("]")

# En base a lo anterior, sabemos que la lista acabará en el índice 22655 + 33 = 22688.
print("Datos relativos a DICIEMBRE:", "\n")
print(data_script[22653:22689], "\n")

# Por tanto, ya tenemos ambos extremos de la lista a extraer del script.
data_to_format = data_script[22281:22689]

# Hagamos algunas modificaciones a los valores que queremos eliminar, con el objetivo
# de únicamente extraer los valores númericos.
data_to_format = data_to_format.replace("[", "")
data_to_format = data_to_format.replace("]", "")
data_to_format = data_to_format.replace('"', "")

# Separamos la variable por comas, para el paso siguiente.
data_to_format = data_to_format.split(",")

# A través de un diccionario, le asignamos a cada mes los datos relativos a cada uno de
# los tres años, aplicando los índices obtenidos tras hacer el split por comas.
dictio = {}
dictio[data_to_format[0]] = data_to_format[1], data_to_format[2], data_to_format[3]
dictio[data_to_format[4]] = data_to_format[5], data_to_format[6], data_to_format[7]
dictio[data_to_format[8]] = data_to_format[9], data_to_format[10], data_to_format[11]
dictio[data_to_format[12]] = data_to_format[13], data_to_format[14], data_to_format[15]
dictio[data_to_format[16]] = data_to_format[17], data_to_format[18], data_to_format[19]
dictio[data_to_format[20]] = data_to_format[21], data_to_format[22], data_to_format[23]
dictio[data_to_format[24]] = data_to_format[25], data_to_format[26], data_to_format[27]
dictio[data_to_format[28]] = data_to_format[29], data_to_format[30], data_to_format[31]
dictio[data_to_format[32]] = data_to_format[33], data_to_format[34], data_to_format[35]
dictio[data_to_format[36]] = data_to_format[37], data_to_format[38], data_to_format[39]
dictio[data_to_format[40]] = data_to_format[41], data_to_format[42], data_to_format[43]
dictio[data_to_format[44]] = data_to_format[45], data_to_format[46], data_to_format[47]

print("El diccionario final de valores luce así:", "\n")
print(dictio, "\n")

# Cargamos la librería pandas, para poder dar al dataset el estilo deseado.
import pandas as pd

# Creamos un dataframe con los datos del diccionario, a través de pd.df.from_dict
matr_turismos = pd.DataFrame.from_dict(dictio)

# Hacemos las modificaciones necesarias para dar forma a los datos.
matr_turismos = matr_turismos.T  # Trasponemos dataset
matr_turismos[0] = pd.to_numeric(matr_turismos[0])
matr_turismos[1] = pd.to_numeric(matr_turismos[1])
matr_turismos[2] = pd.to_numeric(matr_turismos[2])
matr_turismos.columns = ["2021", "2020", "2019"]  # Damos nombre a las columnas.

# Añadimos columnas con variaciones interanuales por mes.
matr_turismos["Variación 2019-2020"] = (matr_turismos["2020"] - matr_turismos["2019"])/matr_turismos["2019"]
matr_turismos["Variación 2019-2021"] = (matr_turismos["2021"] - matr_turismos["2019"])/matr_turismos["2019"]

# Adjuntamos columnas con las evoluciones mensuales de las matriculaciones durante el año.
matr_turismos["Evolución 2019"] = ((matr_turismos["2019"] - matr_turismos["2019"].shift(+1)))/matr_turismos["2019"].shift(+1)
matr_turismos["Evolución 2020"] = ((matr_turismos["2020"] - matr_turismos["2020"].shift(+1)))/matr_turismos["2020"].shift(+1)
matr_turismos["Evolución 2021"] = ((matr_turismos["2021"] - matr_turismos["2021"].shift(+1)))/matr_turismos["2021"].shift(+1)

# Añadimos columnas con las diferencias en evoluciones intermensuales entre los distintos años.
matr_turismos["Difs evolución 19-20"] = (matr_turismos["Evolución 2020"] - matr_turismos["Evolución 2019"])
matr_turismos["Difs evolución 19-21"] = (matr_turismos["Evolución 2021"] - matr_turismos["Evolución 2019"])

print("\n", "El dataset final es el siguiente:", "\n")
print(matr_turismos)

# Almacenamos el resultado en un nuevo archivo CSV.
matr_turismos.to_csv("matr_turismos.csv")

# EXTRA: En las siguientes líneas de código, generamos los gráficos de análisis que serán empleados en el PDF adjunto.

# Cargamos la librería matplotlib.
import matplotlib.pyplot as plt

# Generamos el gráfico.
plt.rcParams["figure.figsize"] = (10,5)
matr_turismos.plot(y=["Variación 2019-2020", "Difs evolución 19-20"], kind="line",
                   title = "Variaciones interanuales por mes y diferencias de evolución intermensual (%)")
