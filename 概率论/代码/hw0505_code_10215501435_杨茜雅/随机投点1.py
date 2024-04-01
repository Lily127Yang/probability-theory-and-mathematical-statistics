#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[35]:


import numpy as np
import math
k=0
n=0
while n<10000000:
 x=np.random.random()
 y=np.random.random()
 n += 1
 if y <= (math.exp(x)-1)/(math.exp(1)-1):
   k+=1
print(k/n)
   


# In[ ]:





# In[ ]:





# In[ ]:




