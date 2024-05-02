#!/usr/bin/env python
# coding: utf-8

# In[4]:


my_list = range(21)
print("Even numbers are ",list(filter(lambda x:x%2==0,my_list)))
print("Odd numbers are ",list(filter(lambda x:x%2!=0,my_list)))


# In[6]:


my_list = range(1,21)
print("Even numbers are ",list(filter(lambda x:x%2==0,my_list)))
print("Odd numbers are ",list(filter(lambda x:x%2!=0,my_list)))


# In[11]:


def even_check(num):
    if num%2==0:
        return True
    
def odd_check(num):
    if num%2!=0:
        return True
    
my_list = range(21)

list(filter(even_check,my_list))
print("Even numbers are ",list(filter(even_check,my_list)))
print("Odd numbers are ",list(filter(odd_check,my_list)))

