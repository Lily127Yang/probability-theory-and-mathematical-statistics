#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math
k=0
n=0
s=0
while n<10000000:
 x=np.random.random()
 n += 1
 s += (math.exp(2*x-1)-math.exp(-1))/(math.exp(1)-math.exp(-1))
print(2*(math.exp(1)-math.exp(-1))*s/n+2*math.exp(-1))
   

