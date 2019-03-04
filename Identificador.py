#!/usr/bin/env python
# coding: utf-8

# In[6]:


Entrada_1 = "678.32 1234 hola mundo234 34 + - "
Arreglo = []
Lista_1 = []
Contador = 0;
Conteo = 0

def Separador(Arreglo, Contador):
    for x in range(len(Entrada_1)):
        Lista_1.insert(x, Entrada_1[x])
        
    Space = 0
    for x in range(Contador,len(Entrada_1)):
        if Entrada_1[x] != ' ':
            Arreglo.insert(Space, Entrada_1[x])
            Space += 1
        else:
            y = x + 1
            break;      
    return y

def Identificador(Arreglo):
    
    #ENTEROS Y REALES
    if '1' <= Arreglo[0] <= '9':
        for x in range(0, len(Arreglo)):  
            if Arreglo[x] == '.':
                a = 1;
                break;
            else:
                a = 0
                
        if a == 1:
            Reales = "".join(Arreglo)
            dic_Real = dict([('Real', Reales)])
            print(dic_Real)
            a = 0
        else:
            Entero = "".join(Arreglo)
            dic_Entero = dict([('Entero', Entero)])
            print(dic_Entero)
            a = 0
    
    #ID'S
    if 'a' <= Arreglo[0] <= 'z':
        for x in range(0, len(Arreglo)):
            ID = "".join(Arreglo)
            dic_ID = dict([('Identificador', ID)])
        print(dic_ID)
        
    #OPERANDOS
    if Arreglo[0] == '+' or Arreglo[0] == '-':
        Operador = "".join(Arreglo)
        dic_Operador = dict([('Operador', Operador)])
        print(dic_Operador)

while Conteo < len(Entrada_1):
    Conteo = Separador(Arreglo, Conteo)
    Identificador(Arreglo)
    del Arreglo[:]


# In[ ]:




