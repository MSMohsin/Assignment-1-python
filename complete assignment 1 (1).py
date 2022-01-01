#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:





# In[3]:


a = "Twinkle, twinkle, little star"
b = "       How I wonder what you are!"
c = "                up above the world so high,"
d = "                like a diamond in the sky."

print(a);
print(b);
print(c);
print(d);
print(a);
print(b);


# In[16]:


print("the python version you are using is:")
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[18]:


import datetime
dt = datetime.datetime.now()
print("current date and time is: " + str(dt));


# In[19]:


area = int(input("input the radius to find the area of circle: "));
calculation = area*area*3.14141

print("The area of the circle according to given radius is: " + str(calculation));


# In[13]:


firstn = str(input("enter your first name: "))
lastn = str(input("enter your last name: "))
print(lastn + " " + firstn);


# In[15]:


print("we are going to add two numbers.")
firstval = int(input("enter first value:"))
secondval = int(input("enter second value:"))
addition = firstval + secondval
print("so the sum of two given numbers is: " + str(addition))


# In[ ]:




