#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn import linear_model


# In[3]:


df=pd.read_csv('carprices.csv')
df


# In[4]:


x=df.drop('Sell Price($)',axis='columns')
x


# In[5]:


y=df['Sell Price($)']
y


# In[6]:


reg=linear_model.LinearRegression()


# In[7]:


reg.fit(x,y)


# In[9]:


# Predict price of car of 4yrs and take mileage about 45000
reg.predict([[45000,4]])


# In[11]:


# Predict price of car of 7yrs and take mileage about 86000
reg.predict([[86000,7]])


# In[16]:


# Model accuracy
reg.score(x,y)


# In[ ]:




