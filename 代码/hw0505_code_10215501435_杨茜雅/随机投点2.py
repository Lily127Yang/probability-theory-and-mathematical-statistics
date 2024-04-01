#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import math
k=0
n=0
while n<10000000:
 x=np.random.random()
 y=np.random.random()
 n += 1
 if y <= ((math.exp(2*x-1)-math.exp(-1))/(math.exp(1)-math.exp(-1))):
   k+=1
print(2*(math.exp(1)-math.exp(-1))*k/n+2*math.exp(-1))
   


# In[ ]:




