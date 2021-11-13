#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# In[3]:


df = pd.read_csv('HR_comma_sep.csv')
df.head()


# In[4]:


pd.crosstab(df.salary,df.left).plot(kind='bar')


# In[12]:


pd.crosstab(df.salary,df.left)


# In[6]:


pd.crosstab(df.Department,df.left).plot(kind='bar')


# In[13]:


pd.crosstab(df.Department,df.left)


# In[34]:


dataEmployee=df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
dataEmployee


# In[37]:


salary_dummies=pd.get_dummies(df.salary)
salary_dummies


# In[48]:


salary_merge=pd.concat([dataEmployee,salary_dummies],axis='columns')
salary_merge


# In[49]:


finaldata=salary_merge.drop("salary",axis='columns')
finaldata


# In[50]:


x=finaldata
x


# In[51]:


y=df.left
y


# In[54]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,train_size=0.3)
model = LogisticRegression()


# In[55]:


model.fit(X_train, y_train)


# In[56]:


model.score(X_test,y_test)


# In[ ]:




