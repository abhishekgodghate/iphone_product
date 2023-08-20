#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 

tournament_file = pd.read_csv("IPL 2022.csv")




# In[8]:


figure = px.bar(tournament_file, x = tournament_file['match_winner'], title = 'Number of Maches won in IPL 2022' )
figure.show()


# In[ ]:


matlab hoga code karna shuru karte hai 


# In[15]:


labels = ['Defending', 'Chasing']
counts = Won_by.values
colors = ['red', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=labels, values=counts)])
fig.update_layout(title_text="Number of matches won by defending or chasing")
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color='black', width=3))
)

fig.show()


# In[17]:


figure = px.bar(tournament_file,x=tournament_file['best_bowling'],title='best bowler in IPL 2022')
figure.show()


# In[25]:


figure = px.bar(tournament_file, x=['player_of_the_match'], title='most player of the match awards')
figure.show()


# In[ ]:




