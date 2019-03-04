#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *

x,y = symbols('x y')
solve([x + y - 25, x*2 - 14],[x , y])

import numpy as np
a = np.array([[3,0,0],
             [1,2,0],
             [0,1,-1]])

b = np.array([30,18,2])
x = np.linalg.solve(a,b)
print(x)

answer = sum(x)
print(answer)


# In[ ]:




