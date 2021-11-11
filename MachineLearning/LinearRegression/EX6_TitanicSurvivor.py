#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


titanic=pd.read_csv('titanic.csv')
titanic.head(30)


# In[49]:


titanicList=titanic[['Survived','Pclass','Name','SibSp','Parch','Fare','Embarked']]
titanicList


# In[50]:


titanicList_dummies=pd.get_dummies(titanicList.Embarked)
titanicList_dummies


# In[51]:


titanicList_concat=pd.concat([titanicList,titanicList_dummies],axis='columns')
titanicList_concat


# In[52]:


titanicData=titanicList_concat.drop("Embarked",axis='columns')
titanicData


# In[53]:


x=titanicData.drop("Name",axis='columns')
y=titanicData.Name


# In[54]:


from sklearn import tree
model=tree.DecisionTreeClassifier()


# In[55]:


model.fit(x,y)


# In[56]:


model.score(x,y)


# In[58]:


model.predict([[1,3,1,0,47.3,0,0,1]])


# In[59]:


model.predict([[1,1,1,0,86.74,0,1,0]])


# In[ ]:




