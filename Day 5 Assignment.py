#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# In[9]:


arr=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
arr.sort()
a=arr
for i in a:
        if(i==0):
            a.remove(each)
            a.append(0)

print(a)


# # Assignment 2

# In[2]:


arr1=[10,20,40,60,70,80]
arr2=[5,15,25,35,45,65]
arr3=[]
i=0
j=0

while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        arr3.append(arr1[i])
        i=i+1
       
    else:
        arr3.append(arr2[j])
        j=j+1
        
arr3=arr3+arr1[i:]+arr2[i:]
print(arr3)


# In[ ]:




