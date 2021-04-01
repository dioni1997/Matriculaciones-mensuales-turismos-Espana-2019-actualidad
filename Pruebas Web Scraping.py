#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, world")


# In[2]:


# 1. Comprobamos los requisitos de crawling del sitio mediante el archivo robots.txt
# https://www.faconauto.com/robots.txt

# 2. Comprobamos el sitemap


# 3. Aplicamos builtwith y whois
import builtwith
import whois

print(whois.whois('https://www.faconauto.com'))


# In[3]:


# Podemos poner que la motivación es ver si la pandemia ha tenido impacto en el número de matriculaciones mensuales.
# Los datos a descargar de la web, están también en PDF, por lo que no se puede calcular con ellos cómodamente.


# In[4]:


import requests
requests.get('https://www.faconauto.com/')


# In[5]:


page = requests.get("https://www.faconauto.com/matriculaciones-mensuales-turismos/")
print(page.content)


# In[6]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content)


# In[7]:


print(soup.prettify())


# In[8]:


soup.title


# In[9]:


soup.p


# In[10]:


soup.a


# In[11]:


soup.find_all('a')


# In[12]:


soup.find_all('text')


# In[13]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[14]:


print(soup.get_text())


# In[15]:


head_tag = soup.head
head_tag.contents


# In[19]:


soup.find(id="post-12055")


# In[27]:


soup.find_all("div", {"class": "g"})


# In[ ]:


<text x="1075.3333333333335" y="71" text-anchor="start" fill="#000000" transform="rotate(-90,1075.3333333333335,71)" style="opacity: 1; cursor: default; font-family: Arial; font-weight: 400; font-size: 13px; font-style: normal;">93.954</text>

<path class="igc-column" d="M620.6666666666666,77v-71.78215a0,0 0 0 1 0,0h21.333333333333336a0,0 0 0 1 0,0v71.78215z" style="fill: rgb(95, 183, 229); stroke-width: 0;"></path>

