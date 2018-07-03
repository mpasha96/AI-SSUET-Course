
# coding: utf-8

# ## QUESTION # 1 : LINEAR REGRESSION

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[65]:

diameters = np.array([6,8,10,14,18])
price = np.array([7,9,13,17.5,18])

variance = diameters.var()
covariance = np.cov(diameters, price, bias=True)[0][1]

beta = covariance/variance
alpha = price.mean() - (beta*diameters.mean())

regression = alpha + beta*diameters
regression


# In[71]:

fig , ax = plt.subplots()
ax.scatter(diameters,price)
ax.plot(diameters,regression, color='red')
plt.title('Regression')


# In[4]:

# Calculating R^2

SS_tot=0
SS_res=0

for i in range(0,5):
    SS_tot += (price[i]-price.mean())**2
    SS_res += (price[i]-regression[i])**2
    
R_sq = 1 - (SS_res/SS_tot)
R_sq


# In[5]:

# Lets validate our answer using skleanr's Linear Regression implementation


# In[6]:

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(diameters.reshape(-1,1),price)
LR.score(diameters.reshape(-1,1),price)


# In[7]:

# We are getting exactly the same value of R^2 score


# In[ ]:




# ## QUESTION # 2 : CLUSTERING

# In[64]:

C1 = np.random.uniform(0.5,1.5,20)
C1 = np.resize(C1,(2,10))
C2 = np.random.uniform(3.5,4.5,20)
C2 = np.resize(C2,(2,10))
C3 = np.vstack((C1,C2))
c1_mean = C1.mean()
c2_mean = C2.mean()
c3_mean = C3.mean()


# In[70]:

x = np.random.uniform(0.0,5.0,40)
x = np.resize(x,(4,10))
plt.scatter(x,C3,color='black')
plt.plot([0,1,2,3,4,5],[c1_mean,c1_mean,c1_mean,c1_mean,c1_mean,c1_mean], color='red',label='C1 Mean')
plt.plot([0,1,2,3,4,5],[c2_mean,c2_mean,c2_mean,c2_mean,c2_mean,c2_mean], color='green',label='C2 Mean')
plt.plot([0,1,2,3,4,5],[c3_mean,c3_mean,c3_mean,c3_mean,c3_mean,c3_mean], color='blue',label='C3 Mean')
plt.title('Clustering')
plt.legend()


# In[ ]:



