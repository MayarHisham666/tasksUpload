#!/usr/bin/env python
# coding: utf-8

# In[1]:


def BinarySearch():
    Orderedset= set(input(" Enter Your list "))
    List= list(Orderedset)
    desired_value = int(input(" Enter Your desired value "))
    #get index of desired_value
    for i in range(len(Orderedset)):
        if List[i] == desired_value:
            deesired_index=i
    LB=0;UB=len(List)
    Ans=(LB+UB)/2
    while List[Ans] != desired_value:
        if List[Ans] < desired_value:
            LB = Ans
            Ans=int((LB+UB)/2)
        elif List[Ans] > desired_value:
            LU  = Ans
            Ans=int((LB+UB)/2)
        else:
            print("Not Found")
    return Ans


# In[ ]:




