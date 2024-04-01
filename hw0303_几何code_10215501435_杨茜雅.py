#!/usr/bin/env python
# coding: utf-8

# In[14]:


from scipy.integrate import dblquad
def areaBetween(a, b, f1, f2):
    one = lambda x, y: 1
    area, _ =dblquad(one, a, b, f1, f2)
    return area

                   
                                        
                                        
                            
                        
f=lambda x: 1.4-x                  
Aarea=areaBetween(0, 1, 0, f)-areaBetween(0, 0.4, 1, f)        
Sarea=areaBetween(0, 1, 0, 1)    
print(Aarea/Sarea)


# In[ ]:





# In[ ]:




