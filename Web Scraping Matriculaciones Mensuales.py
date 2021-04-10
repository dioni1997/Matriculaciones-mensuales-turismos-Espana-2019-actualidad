#!/usr/bin/env python
# coding: utf-8

# In[2]:

# Inspeccionamos la página, y comprobamos que los datos se encuentran en un iframe.
# A través de la librería Selenium, podemos acceder a dicho iframe desde la URL original.

# Cargamos librerías necesarias.
from bs4 import BeautifulSoup
from selenium import webdriver

# Almacenamos la URL original.
url = "https://www.faconauto.com/matriculaciones-mensuales-turismos/"

# Abrimos un webdriver en el navegador Firefox.
# NOTA: Es necesario descargar el ejecutable Geckodriver, a través de: https://github.com/mozilla/geckodriver/releases,
# e incluirlo en el PATH, 
driver1 = webdriver.Firefox()

# Obtenemos la URL a través del driver.
driver1.get(url)

# Encontramos el iframe, clickamos sobre él, y nos cambiamos al directorio correspondiente.
iframeElement = driver1.find_element_by_tag_name("iframe")
iframeElement.click()
driver1.switch_to.frame(iframeElement)

# Creamos un objeto soup a través del driver, una vez nos hemos cambiado de directorio.
soup = BeautifulSoup(driver1.page_source, "html.parser")

# Imprimimos soup.prettify para estudiar la estructura de la URL
print(soup.prettify)

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
# print(soup.prettify)

'''

# In[3]:


# Los números deseados se encuentran almacenados en un tag <script>
# Procedemos a guardar todos estos tags en una nueva variable
scripts_tags = soup.find_all("script")

# Imprimimos la nueva variable para comprobar donde están los datos deseados.
print(scripts_tags)


# In[4]:


# Como los números se encuentran en el quinto tag <script>, lo almacenamos en una nueva variable,
# indexando el quinto valor de scripts_tags.
data_script = scripts_tags[5]
print(data_script)

'''
# En caso de seleccionar la opción sin Selenium, será necesario acceder al 4o tag script.
data_script = scripts_tags[4]
print(data_script)
'''

# In[5]:

import re
import csv

data_script = str(data_script)


# In[6]:

for match in re.finditer("ENERO", data_script):
    print (match.start(), match.end())

# VER SI PUEDO PONER TODA LA EXPRESIÓN DE LISTA ["ENERO"... ] con REGEX
    
print(data_script[22281:22315])

# Poner diciembre, y donde acabe lo ponemos. 
for match in re.finditer("DICIEMBRE", data_script):
    print (match.start(), match.end())

print(data_script[22655])
dic = data_script[22655:]
dic.find("]")

data_script[22688]

data_to_format = data_script[22281:22689]


# In[7]:


print(data_to_format)
data_to_format = data_to_format.replace("[", "")
data_to_format = data_to_format.replace("]", "")
data_to_format = data_to_format.replace('"', "")
print(data_to_format)

data_to_format = data_to_format.split(",")

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

print(dictio)


# In[16]:

# Cargamos librerías necesarias, en este caso utilizamos pandas para crear el dataframe con un estilo con el que poder 
# trabajar.
import pandas as pd

# Creamos un dataframe con los datos del diccionario.
matr_turismos = pd.DataFrame.from_dict(dictio)

# Hacemos las modificaciones necesarias para dar forma a los datos.
matr_turismos = matr_turismos.T
matr_turismos[0] = pd.to_numeric(matr_turismos[0])
matr_turismos[1] = pd.to_numeric(matr_turismos[1])
matr_turismos[2] = pd.to_numeric(matr_turismos[2])
matr_turismos.columns = ["2021", "2020", "2019"]

print(matr_turismos)

# Almacenamos el resultado en un nuevo archivo CSV.
#matr_turismos.to_csv("matr_turismos.csv")

pandaaa = pd.DataFrame.from_dict(dictio)
dataset = pandaaa.T
dataset[0] = pd.to_numeric(dataset[0])
dataset[1] = pd.to_numeric(dataset[1])
dataset[2] = pd.to_numeric(dataset[2])

dataset.columns = ["2021", "2020", "2019"]

# Restamos las columnas para observar la variación que ha habido en las matriculaciones de vehículos realizando la comparativa
# 2019 - 2020; 2019 - 2021 y 2020 - 2021:
dataset["Variacion 2019-2020"] = dataset["2019"] - dataset["2020"]
dataset["Variacion 2019-2021"] = dataset["2019"] - dataset["2021"]
dataset["Variacion 2020-2021"] = dataset["2020"] - dataset["2021"]

# Se puede observar que la tasa de variación es positiva en practicamente todos los meses, al comparar 2019 (año sin covid)
# con respecto a 2020 (año covid), excepto en Julio (mes con más apertura en 2020 respecto a meses anteriores en cuanto
# a medidas y en Diciembre tasa pequeña ya que corresponde a meses de liquidación de vehículos).

#dataset["Variacion"] = dataset.columns[1] - dataset.columns[2]
print(dataset)

# Elaboramos un gráfico que nos muestra esta variación más visual realizandolo sobre la comparativa 2019-2020.

import numpy as np
import matplotlib.pyplot as plt

#dataset_graf = dataset[dataset["2019"]]
#dataset_grafd = dataset[dataset["2020"]]
#plt.hist(dataset_graf, 12, density=True, facecolor='g', alpha=0.76, stacked=True)
#plt.hist(dataset_grafd, 12, density=True, facecolor='r', alpha=0.76, stacked=True)
dataset.plot(x = "2019", y = "2020")

# Quedan aún bastantes cosas, como quitar las comillas que quedan, poner el formato más bonito,
# o limpiar un poco el código. Diego también nos comentó que miráramos buenas prácticas.

# Ver si podemos añadir nuevas columnas de pandas con las variaciones!
