#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn.datasets import load_iris
d = load_iris()


# In[6]:


d.feature_names


# In[7]:


inputs = d.data


# In[8]:


prdictOutput = d.target


# In[10]:


from sklearn.model_selection import train_test_split


# In[11]:


xtrain,xtest,ytrain,ytest= train_test_split(inputs,prdictOutput,train_size=0.2)


# ### model estimator = 10

# In[12]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10)


# In[13]:


model.fit(xtrain,ytrain)


# In[14]:


model.score(xtest,ytest)


# In[15]:


model.feature_importances_


# ### model estimator = 20

# In[16]:


model = RandomForestClassifier(n_estimators=20)


# In[17]:


model.fit(xtrain,ytrain)


# In[18]:


model.score(xtest,ytest)


# ### model estimator = 5

# In[19]:


model = RandomForestClassifier(n_estimators=5)


# In[20]:


model.fit(xtrain,ytrain)


# In[21]:


model.score(xtest,ytest)


# ### model estimator = 30

# In[22]:


model = RandomForestClassifier(n_estimators=30)


# In[23]:


model.fit(xtest,ytest)


# In[24]:


model.score(xtest,ytest)


# In[25]:


model.feature_importances_


# In[ ]:




