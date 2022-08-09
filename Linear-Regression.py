#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Linear-Regression


# In[ ]:


Importing All the Required Libraries


# In[4]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


Reading CSV File


# In[6]:


df= pd.read_csv('Height-Weight Data.csv')
df


# In[ ]:


Checking Header File


# In[9]:


df.head()


# In[ ]:


Check Header Tail Function


# In[10]:


df.tail()


# In[ ]:


Checking header Serial two 


# In[11]:


df.head(2)


# In[ ]:


Checking Height


# In[13]:


df.Height


# In[ ]:


Checking Weight


# In[14]:


df.Weight


# In[ ]:


Checking Height Mean


# In[20]:


df.Height.mean() 


# In[ ]:


Checking Weight Mean


# In[21]:


df.Weight.mean() 


# In[ ]:


All File Describing 


# In[23]:


df.describe()


# In[ ]:


Checking Null Value of data


# In[24]:


df.isnull().sum()


# In[ ]:


Plot The Data


# In[39]:


plt.figure(figsize=(12,8))
plt.scatter(df.Height,df.Weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.title('Height',color='red')


# In[44]:


x=df[['Height']]
y=df[['Weight']]


# In[ ]:


Defing X Header


# In[47]:


x.head()


# In[ ]:


Defing Y Header


# In[48]:


y.head()


# In[ ]:


Train and Test data


# In[49]:


from sklearn.model_selection import train_test_split as tts


# In[ ]:


xtrain,xtest,ytrain,ytest=tts(x,y,test_size=.30)


# In[ ]:


X Train Model


# In[53]:


xtrain.head()


# In[ ]:


Y Train Model


# In[54]:


ytrain.head()


# In[ ]:


Data into Array


# In[59]:


x=np.array(df.Height).reshape(-1, 1)
y=np.array(df.Weight).reshape(-1, 1)
x


# In[ ]:





# In[71]:


df['Weighit'] = (x)
df.head()


# In[ ]:


Predict Value


# In[ ]:


Value oF Height


# In[76]:


x= input("Enter the value of Height : ")

print("Your predicted value is : ",y)


# In[ ]:


Value oF Weight


# In[77]:


x= input("Enter the value of Weight : ")

print("Your predicted value is : ",y)


# In[ ]:




