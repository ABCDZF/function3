#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
data =[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)


# In[3]:


#2
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_data = list(map(lambda x:x**2,data))
print(square_data)


# In[4]:


#3
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_data = tuple(map(lambda x: str(x),data))
print(tuple_data)


# In[5]:


#4

from functools import reduce
numbers = list(range(1, 26))
product = reduce(lambda x, y: x * y, numbers)
print(product)


# In[9]:


#5
data =[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
filtre_data = list(filter(lambda x: x%2==0 and x%3==0,data))
print(filtre_data)


# In[10]:


#6

strings = ['python', 'php', 'aba', 'radar', 'level']

palindromes = list(filter(lambda x: x == x[::-1], strings))

print(palindromes)


# In[ ]:




