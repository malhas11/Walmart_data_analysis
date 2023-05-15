---
title: "Walmark EDA"
author: "Saad"
date: "15/05/2023"
---

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Walmart Data Analysis and Forcasting.csv")


# In[3]:


data.head(6)


# In[4]:


data.tail(6)


# In[5]:


data.describe()


# In[6]:


data.isna().sum()


# In[9]:


data.shape


# In[13]:


data.info()


# In[17]:


grouped = data.groupby("Store").agg({"Weekly_Sales":"sum"}).sort_values("Weekly_Sales",ascending=True).head(5)


# In[18]:


grouped


# In[23]:


#temp and weekly sales
plt.scatter(data["Temperature"], data["Weekly_Sales"], alpha=0.5)
plt.xlabel("Temperature")
plt.ylabel("Weekly Sales")
plt.title("Scatter plot of weekly sales vs Temperature")


# In[24]:


#trend line weekly sales
data["Date"] = pd.to_datetime(data["Date"], format = '%d-%m-%Y')


# In[26]:


WeeklySales = data.groupby(["Date"])["Weekly_Sales"].sum().reset_index()


# In[29]:


plt.figure(figsize=(12, 8))
plt.plot(WeeklySales["Date"], WeeklySales["Weekly_Sales"],color="red")
plt.xlabel("Date")
plt.ylabel("Weekly Sales")
plt.title("Weekly Sales trend line")
plt.show()


# In[33]:


# distribution of weekly sales
sns.histplot(data['Weekly_Sales'], bins= 50, color="blue", edgecolor="black", kde=True)
plt.title("Distribution of Weekly Sales")
plt.show()


# In[35]:


#cor plot
plt.figure(figsize=(12, 7))
sns.heatmap(data.corr(), annot = True, vmin = -1, vmax = 1)
plt.show()

