#!/usr/bin/env python
# coding: utf-8

# In[1]:


abc = "abcdefghijklmnopqrstuvwxyz"
oracion = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb."
list_resp = []
t_abc = list(abc)
t_oracion = list(oracion)
s = 0
p = 0
x = 0
y = 0

for x in oracion:
    s = s + 1
    for y in abc:
        p = p + 1
        if x == y:
            list_resp.insert(s,t_abc[p+1]) 
            p = 0
            break;
        if x == " ":
            list_resp.insert(s, " ")
            p = 0
            break;
        if x == "y":
            list_resp.insert(s, t_abc[0])
            p = 0
            break;
        if x == "z":
            list_resp.insert(s, t_abc[1])
            p = 0
            break;
        if x == "." or x == "(" or x == ")" or x == "'":
            list_resp.insert(s, x)
            p = 0
            break;

respuesta = "".join(list_resp)
print(respuesta)


# In[ ]:




