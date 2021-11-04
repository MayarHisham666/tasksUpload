#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn import linear_model
import joblib


# In[3]:


#This function is use for only general numbers data model(No strings)
def linearRegression(fileName,column1,column2):
    df=pd.read_csv(fileName)
    x=df.drop(column2,axis='columns')
    y=df[column2]
    reg= linear_model.LinearRegression()
    reg.fit(x,y)
    return reg.coef_


# In[ ]:




