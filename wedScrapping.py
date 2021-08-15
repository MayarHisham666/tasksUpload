#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[2]:


source= requests.get("https://coreyms.com/").text


# In[3]:


source


# In[4]:


soup = BeautifulSoup(source,'lxml')


# In[5]:


print(soup.prettify())


# In[7]:


articles = soup.find_all('article')
for article in articles:
    headline = article.h2.a.text
    print(headline +'\n')
    summary = article.find('div',class_="entry-content").p.text
    print(summary + '\n')
    try :
        vid = article.find('iframe', class_= "youtube-player")['src']
        vid_id = vid.split('/')
        video = vid_id[4].split('?')
        c =video[0]
        ytLink = f'https://youtube.com/watch?v={c}'
    except Exception as e:
        print ("there was an error with the youtube link")
    print(ytLink + '\n')
    csvfile = open ('scrape1.csv', 'w', encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(['headline', 'summary', 'link'])
    writer.writerow([headline, summary, ytLink])
csvfile.close()  


# In[ ]:




