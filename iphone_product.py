#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv("apple_products.csv")


# In[3]:


print(data.isnull().sum())


# In[4]:


print(data.describe())


# In[5]:


highest_rated=data.sort_values(by = ["Star Rating"],ascending = False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# In[6]:


iphones = highest_rated['Product Name'].value_counts()

labels = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated,x=labels,y=counts,
               title="number of ratings and product name")
figure.show()


# In[7]:


iphones = highest_rated['Product Name'].value_counts()

labels = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated,x=labels,y=counts,
               title="number of reviews and product name")
figure.show()


# In[17]:


import plotly.express as px

figure = px.scatter(data_frame=data, x="Number Of Ratings",
                   y="Sale Price", size_max="Discount Percentage", trendline="ols",
                   title="Relationship between sale price and number of ratings")
figure.show()


# In[19]:


figure = px.scatter(data_frame=data, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price", trendline="ols",
                    title="Relationship between discount percentage and Number of rating")
figure.show()


# In[ ]:


Objectives 
data jo hai vo clean hai ya nahi 
data anlysis 
data visualize
project explain

