#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

n=0
k=0
while n<100000:
  a=np.random.random()
  b=np.random.random()
  n += 1
  if a+b <1.4:
    k += 1
p=k/n
print(p)


# In[ ]:




