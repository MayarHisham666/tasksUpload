#!/usr/bin/env python
# coding: utf-8

# # Project - $k$-Nearest-Neighbors Classifier
# - Create a $k$-Nearest-Neighbors Classifier supporting 3 dimensions
# - Investigate whether it performs better

# ### Step 1: Import libraries

# In[1]:


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


# ### Step 2: Read data
# - Use pandas [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) method to read **files/weather.csv**
# - HINT: Use **parse_dates=True** and **index_col=0**

# In[5]:


data=pd.read_csv('files/weather.csv',parse_dates=True,index_col=0)
data


# In[ ]:





# ### Step 3: Investigate data types
# - Use [dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)
# - The goal is to identify all columns with datatype **float64** for next step

# In[6]:


data.dtypes


# In[ ]:





# ### Step 4: Choose 3 columns to create datasets
# - Use **Humidity3pm** and **Pressure3pm** together with another column to predict **RainTomorrow**
# - Make a list of three column names **'Humidity3pm', 'Pressure3pm', INSERT YOUR CHOICE** (should be one with dtype *float64*, e.g., **Cloud3pm**), and **'RainTomorrow'**
# - Create the dataset consisting of these 4 columns

# In[7]:


weather=data[['Humidity3pm','Pressure3pm','Cloud3pm','RainTomorrow']]
weather


# In[ ]:





# ### Step 5: Deal with remaining missing data
# - A simple choice is to simply remove rows with missing data
# - Use [dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)

# In[18]:


weather_clean=weather.dropna()


# In[19]:


weather_clean.head()


# ### Step 6: Create training and test datasets
# - Define dataset **X** to be the data consisting of the three columns.
# - Define dataset **y** to be datset cosisting of **'RainTomorrow'**.
#     - HINT: Use list comprehension to transform **'No'** and **'Yes'** to 0 and 1, repectively (like in the Lesson)
# - Divide into **X_train, X_test, y_train, y_test** with **train_test_split**
#     - HINT: See how it is done in Lesson
#     - You can use **random_state=42** (or any other number) if you want to reproduce results.

# In[20]:


x=weather_clean[['Humidity3pm','Pressure3pm','Cloud3pm']]
rain=weather_clean[['RainTomorrow']]
rain_dummies = pd.get_dummies(rain.RainTomorrow)
rain_concat=pd.concat([rain,rain_dummies],axis=1)


# In[21]:


rain_concat


# In[22]:


y = rain_concat.drop('RainTomorrow',axis=1)
y


# ### Step 7: Train and test the model
# - Create classifier with **KNeighborsClassifier**
#     - You can play around with n_neighbors (default =5)
# - Fit the model with training data **(X_train, y_train**)
# - Predict data from **X_test** (use predict) and assign to **y_pred**.
# - Evalute score by using **metrics.accuracy_score(y_test, y_pred)**.

# In[23]:


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[25]:


model=KNeighborsClassifier()
model.fit(X_train,y_train)
y_predict=model.predict(X_test)


# In[28]:


model.score(X_train,y_train)


# In[27]:


model.score(X_test,y_test)


# In[30]:


model.predict([[84.0, 1017.4, 8.0 ]])


# In[26]:


metrics.accuracy_score(y_test,y_predict)


# ### Step 8 (Optional): Try with different columns
# - You can redo with diffrent choise of columns (starting from step 4)

# In[ ]:





# In[ ]:





# In[ ]:




