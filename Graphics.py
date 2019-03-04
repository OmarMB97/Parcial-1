#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt 
from numpy import *

x = arange(0.0, 10, 0.01)
y = sin(e**x) - cos(x)
plt.plot(x,y)
plt.grid(axis = 'both')


# In[ ]:




