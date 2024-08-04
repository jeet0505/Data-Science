#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_health_premium(gender,date_of_birth,smoker):
    if gender=='male':
        if 1990 <= date_of_birth <=2000:
            if smoker == "yes":
                print("Your annual premium is Rs.35000/-")
            else:
                print("Your annual premium is Rs.31500/-")
        elif 1970 <= date_of_birth <=1990:
            if smoker == "yes":
                print("Your annual premium is Rs.40000/-")
            else:
                print("Your annual premium is Rs.38000/-")
                
    elif gender=='female':
        if 1990 <= date_of_birth <=2000:
            if smoker == "yes":
                print("Your annual premium is Rs.30000/-")
            else:
                print("Your annual premium is Rs.27000/-")
        if 1970 <= date_of_birth <=1990:
            if smoker == "yes":
                print("Your annual premium is Rs.35000/-")
            else:
                print("Your annual premium is Rs.33250/-")
            
               
            
        


# In[2]:


calculate_health_premium('male',1995,'yes')


# In[3]:


calculate_health_premium('female',1995,'no')


# In[ ]:




