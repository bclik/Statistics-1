#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

ornek = pd.DataFrame()


# In[2]:


ornek["yas"] = np.append(np.random.normal(23,1,50), np.random.normal(35,1,50))


# In[3]:


ornek["maas"] = np.append(np.random.normal(3500,50,50), np.random.normal(5500,50,50))


# In[5]:


ornek["cinsiyet"] = ["kadin"]*50 + ["erkek"]*50


# In[6]:


ornek


# In[7]:


ornek.yas.mean()


# In[9]:


sum(ornek.yas)/len(ornek.yas)


# In[11]:


import statistics
print(statistics.median(ornek.maas))


# In[12]:


print(np.median(ornek.maas))


# In[14]:


import statistics
statistics.mode(ornek.yas)


# not : sayılar benzersin olduğundan ve tekrar etmediğinden mode çalışmamıştır.

# In[15]:


print(np.var(ornek.maas,ddof=1))


# In[16]:


print(ornek.maas.var())


# In[17]:


np.std(ornek.yas,ddof=1)


# In[18]:


ornek.yas.std()


# In[19]:


np.std(ornek.yas, ddof=1)/np.sqrt(len(ornek.yas))


# In[ ]:




