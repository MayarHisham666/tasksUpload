#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('homeprices.csv')
df


# In[4]:


df.bedrooms.fillna(df.bedrooms.median(),inplace=True)
df


# In[5]:


x=df.drop('price',axis='columns')
x


# In[6]:


y=df.price
y


# In[7]:


reg = linear_model.LinearRegression()


# In[8]:


reg.fit(x,y)


# In[9]:


reg.predict([[2500,4.0,6]])


# # Excersice 2

# In[2]:


hire = pd.read_csv('hiring.csv')
hire


# In[3]:


hire['test_score(out of 10)'].fillna(hire['test_score(out of 10)'].median(),inplace=True)
hire


# In[4]:


hire.loc[0,'experience']='nine'
hire.loc[1,'experience']='sex'
hire


# In[5]:


hire.replace(to_replace=['two','three','five','sex','seven','nine','ten','eleven'],value=[2,3,5,6,7,9,10,11],inplace=True)


# In[6]:


hire


# In[7]:


x=hire.drop('salary($)',axis='columns')
y=hire['salary($)']


# In[8]:


reg2=linear_model.LinearRegression()


# In[9]:


reg2.fit(x,y)


# In[11]:


reg2.score(x,y)


# In[ ]:




