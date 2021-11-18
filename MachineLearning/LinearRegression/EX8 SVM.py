#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.datasets import load_digits


# In[8]:


d = load_digits()


# In[11]:


d.target_names


# In[12]:


d.data


# In[13]:


d.target


# In[14]:


df=pd.DataFrame(d.data,columns=d.feature_names)
df


# In[15]:


df.describe()


# In[17]:


df.isna().sum()


# In[20]:


df.dtypes


# ###  Test size of samples is 20%

# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


x_train,x_test,y_train,y_test = train_test_split(d.data,d.target,test_size=0.2)


# ### SUPPORT VECTOR MACHINE SVM

# In[23]:


from sklearn.svm import SVC


# In[24]:


model=SVC()
model.fit(x_train,y_train)


# In[25]:


model.score(x_test,y_test)


# ### SVM USING LINER KERNAL & RBF

# In[26]:


model_linear_kernal=SVC(kernel='linear')
model_linear_kernal.fit(x_train,y_train)


# In[27]:


model_linear_kernal.score(x_test,y_test)


# In[28]:


model_rbf_kernal=SVC(kernel='rbf')


# In[29]:


model_rbf_kernal.fit(x_train,y_train)
model_rbf_kernal.score(x_test,y_test)


# ### SVM USING REQULARLIZATION
# 

# In[30]:


modelR=SVC(C= 1)
modelR.fit(x_train,y_train)
modelR.score(x_test,y_test)


# In[37]:


modelR=SVC(C= 0.2)
modelR.fit(x_train,y_train)
modelR.score(x_test,y_test)


# In[35]:


modelR=SVC(C= 0.09)
modelR.fit(x_train,y_train)
modelR.score(x_test,y_test)


# ### SVM USING GAMMA PARAMETER

# In[38]:


modelG=SVC(gamma=5)
modelG.fit(x_train,y_train)
modelG.score(x_test,y_test)


# In[48]:


modelG=SVC(gamma=0.0001)
modelG.fit(x_train,y_train)
modelG.score(x_test,y_test)


# In[ ]:




