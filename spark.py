#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries
import pandas as pd 
import numpy
import matplotlib.pyplot as plt 
from pyspark.sql import SparkSession


# In[13]:


get_ipython().system('pip install pymysql')


# In[44]:


import pymysql
conn = pymysql.connect(host='db', user='root', passwd='123', db='invest')
cursor = conn.cursor()
cursor.execute("select * from invest_perfil limit 100;")


# In[45]:


data=cursor.fetchall()


# In[47]:


print(data)


# In[54]:


from pyspark.sql import SparkSession

spark = SparkSession     .builder     .appName("Python Spark SQL basic example")     .config("spark.some.config.option", "some-value")     .getOrCreate()


# In[58]:


df = spark.createDataFrame(data , ["id", "name", "year", "city"])


# In[59]:


df.show()

