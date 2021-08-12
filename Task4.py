#!/usr/bin/env python
# coding: utf-8

# In[12]:


def get_UnorderedSet(list):
    new_list=[]
    for i in range(0,len(list)):
        # loop for values of input list
        value=list[i]
        dup=0
        if(i == 0):
            new_list.append(value)
        else:
            for j in range(len(new_list)):
                #Checks duplication
                if(value == new_list[j]):
                    dup=1
        if(dup == 0 and i>0):
            new_list.append(value)
    return new_list  


# In[13]:


list=[1,1,1,3,2,6,7,7,7,6,2,3]
get_UnorderedSet(list)


# In[14]:


list=[80,80,10,30,20,60,70,70,70,60,20,30,10,10,20,40,40,]
get_UnorderedSet(list)


# In[ ]:




