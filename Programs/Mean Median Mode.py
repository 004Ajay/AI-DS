import math

data = [9, 10, 12, 13, 13, 13, 15, 15, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]
leng = len(data)

# ----------------------------------------------------------------------------------- #

# Mean
mean = sum(data)/leng
print("Mean:", mean)

# ----------------------------------------------------------------------------------- #

# Median
_sorted = sorted(data)
if leng % 2 == 0: # if length of dataset is an even number
    loc1 = int(leng/2)
    loc2 = int((leng/2)+1)
    med = (data[loc1] + data[loc2]) / 2
    print("Median:", med)
else: # if length of dataset is an odd number
    loc = int((leng+1)/2)
    print("Median: ", _sorted[loc])

# ----------------------------------------------------------------------------------- #

# Mode
dic = {}

for i in data:
    dic[i] = data.count(i) 

key_list = list(dic.keys())
val_list = list(dic.values())

pos = val_list.index(max(val_list))
print("Mode:", key_list[pos]) # print key with max value

# ----------------------------------------------------------------------------------- #

# Standard Deviation
# SD = sqrt[( sigma(Xi - X_bar) ^ 2) / length]

sq = []

for i in data:
    sq.append((i-mean)**2)
    
ins_sqrt = sum(sq)/leng
sd = math.sqrt(ins_sqrt)
print("Standrad Deviation:", round(sd, 4))

# ----------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------- #

# USING LIBRARY FUNCTION

import statistics as st # mean, median, mode
import numpy as np # standard deviation, percentile
import matplotlib.pyplot as plt # data distributions

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