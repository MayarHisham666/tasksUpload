#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=['R',10,'R',20,'R','R',30,40,50,60,'R','R','R',70,'R',80,90,100,'R','R']

# In[13]:


for i in range(len(list)):
    if list[i] == 'R':
        del list[i]


# In[14]:


list


# In[ ]:




