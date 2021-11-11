#!/usr/bin/env python
# coding: utf-8

# In[20]:


from sklearn.datasets import load_digits
digit=load_digits()


# In[21]:


dir(digit)


# In[22]:


#Number of images
len(digit.images)


# In[23]:


# Overall data values
digit.data[15]


# In[24]:


# Value of digit number on the image
digit.target[15]


# # Logistic Regression

# In[25]:


x=digit.data
y=digit.target


# In[26]:


from sklearn.linear_model import LogisticRegression
model= LogisticRegression()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[27]:


model.fit(x_train,y_train)


# In[28]:


model.score(x_train,y_train)


# In[29]:


model.score(x_test,y_test)


# In[30]:


y_prdicted=model.predict(x_test)
y_prdicted


# In[31]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_prdicted)
cm


# In[32]:


from sklearn.datasets import load_iris
d = load_iris()


# In[33]:


dir(d)


# In[34]:


len(d.data)


# In[35]:


d.feature_names


# In[36]:


x_data=d.data
y_data=d.target


# In[38]:


flower=LogisticRegression()
x_dataTrain,x_dataTest,y_dataTrain,y_dataTest=train_test_split(x_data,y_data,test_size=0.2)


# In[39]:


flower.fit(x_dataTrain,y_dataTrain)


# In[41]:


flower.score(x_dataTrain,y_dataTrain)


# In[44]:


flower.score(x_dataTest,y_dataTest)


# In[45]:


y_dataPredicted=flower.predict(x_dataTest)
y_dataPredicted


# In[54]:


flower.predict([[12,4,17,6]])


# In[57]:


flower.predict([[100,6,200,10]])


# In[ ]:




