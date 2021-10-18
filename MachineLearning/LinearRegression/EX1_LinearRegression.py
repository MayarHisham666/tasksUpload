#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[19]:


df = pd.read_csv('homeprices1.csv')
df


# In[20]:


print(df.area.min())
print(df.area.max())


# In[21]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area,df.price,color='r',marker='x')


# In[22]:


area=df.drop('price',axis='columns')
area           


# In[23]:


price=df.price
price


# In[24]:


reg = linear_model.LinearRegression()
reg.fit(area,price)


# In[25]:


reg.predict([[3000],[3750]])


# In[27]:


reg.coef_ # m coeff


# In[28]:


reg.intercept_ # y intercept


# In[29]:


area2= pd.read_csv('areas.csv')
area2


# In[30]:


p=reg.predict(area2)
p


# In[31]:


area2['price']=p
area2


# In[32]:


area2.to_csv("Prediction.csv",index=False)


# # Excersice 1

# In[39]:


income=pd.read_csv('canada_per_capita_income.csv')
income


# In[40]:


income.columns


# In[49]:


year=income.drop('per capita income (US$)',axis='columns')
year


# In[50]:


canadian_income=income['per capita income (US$)']
canadian_income                       


# In[51]:


reg2= linear_model.LinearRegression()
reg2.fit(year,canadian_income)


# In[52]:


reg2.predict([[2020]])


# In[ ]:




