#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


port1={21:"FTP",22:'SSH',23:'telnet',80:"http"}
port1={value:key for key,value in port1.items()}
print(port1)


# # Question 2

# In[2]:


liss=[(1,2),(3,4),(5,6),(4,5)]

for i in range(len(liss)):
    liss[i]=sum(liss[i])
print(liss)


# # Question 3

# In[3]:


lis=[(1,2,3),[1,2],['a','hit','less']]


ils=[x for i in lis for x in i] 
print(ils)


# In[ ]:




