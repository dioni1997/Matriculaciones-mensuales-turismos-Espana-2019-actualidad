#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Inspeccionamos la página, y comprobamos que los datos se encuentran en un iframe.
# A través del parámetro "src", podemos acceder al enlace en el que se encuentran estos datos.
# Este será el enlace que usaremos para el web scraping.

# Pregunta para el profesor: 
# ¿Es necesario emplear Selenium para obtener el documento iframe directamente?
# Ya que estamos teniendo muchos problemas, por ejemplo con BeautifulSoup no mostrando el "src"
# (no se muestran todos los elementos del tag correspondiente), o con el ejecutable "Geckodriver".

# Cargamos librerías necesarias
import requests
from bs4 import BeautifulSoup

# Prueba de respuesta HTTP
page = requests.get("https://e.infogram.com/580ba5d8-99b4-4262-86ae-e335e3a02a5b?parent_url=https%3A%2F%2Fwww.faconauto.com%2Fmatriculaciones-mensuales-turismos%2F&amp;src=embed#async_embed")
print("Código de respuesta HTTP:", page)

# Almacenamos el objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Imprimimos soup.prettify para estudiar la estructura de la URL
print(soup.prettify)


# In[3]:


# Los números deseados se encuentran almacenados en un tag <script>
# Procedemos a guardar todos estos tags en una nueva variable
scripts_tags = soup.find_all("script")

# Imprimimos la nueva variable para comprobar donde están los datos deseados.
print(scripts_tags)


# In[4]:


# Como los números se encuentran en el cuarto tag <script>, lo almacenamos en una nueva variable,
# indexando el cuarto valor de scripts_tags.
data_script = scripts_tags[4]
print(data_script)


# In[5]:


# Próximos pasos - almacenar los datos en un CSV para trabajar con ellos.
# Posible idea: separar campos por comas, filtrar por listas que incluyan
# los meses del año (ENERO, FEBRERO, MARZO...)

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
print(data_to_format)

data_to_format = data_to_format.split(",")
print(data_to_format)

lists = []
lists.append(data_to_format[0:4])
lists.append(data_to_format[4:8])
lists.append(data_to_format[8:12])
lists.append(data_to_format[12:16])
lists.append(data_to_format[16:20])
lists.append(data_to_format[20:24])
lists.append(data_to_format[24:28])
lists.append(data_to_format[28:32])
lists.append(data_to_format[32:36])
lists.append(data_to_format[36:40])
lists.append(data_to_format[40:44])
lists.append(data_to_format[44:48])

print(lists)

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


with open("matr_turismos.csv", "w") as csvfile: 
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter = ",")
    wr.writerow(lists)
    
# Problema: el formato me queda todo en la misma línea

'''
print(wr)
with open("prueba_dictio", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = dictio.keys())
        writer.writeheader()
        for k in dictio:
            writer.writerow(k)
'''   

# No terminado.
# Al parecer, estoy teniendo problemas porque hay que pasar primero el dict a pandas.
# https://www.reddit.com/r/learnpython/comments/avj6d2/ive_looked_on_stack_overflow_and_a_bunch_of_other/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html

# Quizás una vez lo pase a pandas, ya vaya

import pandas as pd

pandaaa = pd.DataFrame.from_dict(dictio)
print(pandaaa)


# In[18]:


pandaaa.to_csv("pandaaa.csv")

# Quedan aún bastantes cosas, como quitar las comillas que quedan, poner el formato más bonito,
# o limpiar un poco el código. Diego también nos comentó que miráramos buenas prácticas.

# Ver si podemos añadir nuevas columnas de pandas con las variaciones!
