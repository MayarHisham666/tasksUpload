#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


titanic=pd.read_csv('titanic.csv')
titanic.head(30)


# In[3]:


titanicList=titanic[['Survived','Pclass','Name','SibSp','Parch','Fare','Embarked']]
titanicList


# In[4]:


titanicList_dummies=pd.get_dummies(titanicList.Embarked)
titanicList_dummies


# In[5]:


titanicList_concat=pd.concat([titanicList,titanicList_dummies],axis='columns')
titanicList_concat


# In[6]:


titanicData=titanicList_concat.drop("Embarked",axis='columns')
titanicData


# In[7]:


x=titanicData.drop("Name",axis='columns')
y=titanicData.Name


# In[8]:


from sklearn import tree
model=tree.DecisionTreeClassifier()


# In[9]:


model.fit(x,y)


# In[10]:


model.score(x,y)


# In[11]:


model.predict([[1,3,1,0,47.3,0,0,1]])


# In[12]:


model.predict([[1,1,1,0,86.74,0,1,0]])


# In[79]:


tt=titanic[['Pclass','Sex','Age','Fare',]]
tt.head(10)


# In[80]:


tt.fillna(0.0,inplace=True)
tt.head(10)


# In[81]:


from sklearn.preprocessing import LabelEncoder
tt['sex_n']=LabelEncoder().fit_transform(tt.Sex)
td=tt.drop('Sex',axis='columns')
td


# In[89]:


inputs=td.drop('sex_n',axis='columns')
inputs


# In[90]:


target=td.sex_n
target


# In[91]:


modelII=tree.DecisionTreeClassifier()


# In[92]:


modelII.fit(inputs,target)


# In[93]:


modelII.score(inputs,target)


# In[94]:


modelII.predict([[3,22,54.000]])


# In[95]:


modelII.predict([[2,7,8.700]])


# In[ ]:




