#!/usr/bin/env python
# coding: utf-8

# In[1]:

# La URL que contiene los datos deseados, en forma de barras, es la siguiente:
# https://www.faconauto.com/matriculaciones-mensuales-turismos/

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


# In[2]:


# Los números deseados se encuentran almacenados en un tag <script>
# Procedemos a guardar todos estos tags en una nueva variable
scripts_tags = soup.find_all("script")

# Imprimimos la nueva variable para comprobar donde están los datos deseados.
print(scripts_tags)


# In[3]:


# Como los números se encuentran en el cuarto tag <script>, lo almacenamos en una nueva variable,
# indexando el cuarto valor de scripts_tags.
data_script = scripts_tags[4]
print(data_script)


# In[4]:


# Próximos pasos - almacenar los datos en un CSV para trabajar con ellos.
# Posible idea: separar campos por comas, filtrar por listas que incluyan
# los meses del año (ENERO, FEBRERO, MARZO...)

