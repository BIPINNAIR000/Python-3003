#!/usr/bin/env python
# coding: utf-8

# # Sum of n natural number using while loop

# In[2]:


n=int(input("Enter a number: "))
sum1=0
while(n>0) :
    sum1=sum1+n
    n=n-1
print("The sum of n natural number is",sum1)


# # To check prime or not

# In[7]:


num=int(input("Enter a number: "))
for i in range (2, num):
    if num %i==0:
        print("not prime number")
        break
    else :
            print("prime number")
    


# In[ ]:




