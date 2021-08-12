#!/usr/bin/env python
# coding: utf-8

# In[1]:


class VisaCard:
    def __init__(self):
        self.__name= "  "
        self.__visa= 0
        self.__password = " "
    def addMoney(self):
        Money = float(input(" Please enter amount of money you want to add :"))
        self.__visa+=Money
    def withdrawAccount(self,amountOfmoney):
        if (amountOfmoney<self.__visa):
            self.__visa-=amountOfmoney
            print("You have successfully withdraw ",str(amountOfmoney)," From ur Visa")
        elif(amountOfmoney==self.__visa):
            print("You have limit charge visa.. Are you sure you want drawout that amount of money yes or no")
            answer=input()
            if(answer == "yes"):
                self.__visa-=amountOfmoney
            else:
                print("Your operation has been canceled !")
        else:
            print("Sorry ! You have no enough money")
            


# In[2]:


data = " "
with open ("VisaCard.txt","rb") as txt:
    data = txt.readlines()


# In[3]:


data


# In[ ]:




