#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math


# In[17]:


data = [9, 10, 12, 13, 13, 13, 15, 15, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]
leng = len(data)


# ## Mean

# In[18]:


mean = sum(data)/leng
print("Mean:", mean)


# ## Median

# In[27]:


_sorted = sorted(data)

if leng % 2 == 0: # if length of dataset is an even number
    loc1 = int(leng/2)
    loc2 = int((leng/2)+1)
    print("Median:", loc1, "&", loc2)
else: # if length of dataset is an odd number
    loc = int((count+1)/2)
    print("Median: ", _sorted[loc])



# ## Mode

# In[20]:


dic = {}

for i in data:
    dic[i] = data.count(i) 

key_list = list(dic.keys())
val_list = list(dic.values())

pos = val_list.index(max(val_list))
print("Mode:", key_list[pos]) # print key with max value


# ## Standard Deviation

# ## SD = $\sqrt\frac{∑∣x−μ∣^2}{N}\$  
# #### *x = Individual data elements*<br>*μ = Mean*<br>*N = Number of elements in dataset*

# In[24]:


sq = []

for i in data:
    sq.append((i-mean)**2)
    
ins_sqrt = sum(sq)/leng
sd = math.sqrt(ins_sqrt)
print("Standrad Deviation:", round(sd, 4))


# ## Percentile

# In[ ]:





# ## Data Distributions

# ## All in One

# In[29]:


# ** run all other cell before this. ** 

print("Mean:", mean)
# ------------------------------------------------------ #
if leng % 2 == 0: 
    print("Median:", loc1, "&", loc2)
else:
    print("Median: ", _sorted[loc])
# ------------------------------------------------------ #    
print("Mode:", key_list[pos])
# ------------------------------------------------------ #
print("Standrad Deviation:", round(sd, 4))
# ------------------------------------------------------ #
print("Percentile:", mean)


# In[ ]:


"""
USING LIBRARY FUNCTION

import statistics as st # mean, median, mode
import numpy as np # standard deviation, percentile
import matplotlib.pyplot as plt # data distributions

data = [1,2,3,4,5]

#mean
print("Mean: ", st.mean(data))

#median
print("Median: ", st.median(data))

#mode
print("Mode: ", st.mode(data))

#standard deviation
print("Standard Deviation: ", np.std(data))

#percentile
print("Percentile: ", np.percentile(data, 50))

# ---------------------------------------------------------------------------------- #

#uniform distribution
uniform_data = np.random.uniform(0,1,10000)
plt.hist(uniform_data)
plt.show()

#normal distribution
normal_data = np.random.normal(0,1,10000)
plt.hist(normal_data)
plt.show()

#binomial distribution
binomial_data = np.random.binomial(1,0.5,10000)
plt.hist(binomial_data)
plt.show()

#poisson distribution
poisson_data = np.random.poisson(1,10000)
plt.hist(poisson_data)
plt.show()

"""
