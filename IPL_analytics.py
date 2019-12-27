#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


ipl_df = pd.read_csv('IPLIMB381IPL2013.csv')


# In[47]:


ipl_df


# In[7]:


type(ipl_df)   


# In[8]:


pd.set_option('display.max_columns',7) 
# display oNLY first


# In[11]:


ipl_df.head(5)


# In[15]:


ipl_df.columns
ipl_df.head(5).transpose()


# In[13]:


ipl_df.head(5).transpose()


# In[16]:


ipl_df.shape


# In[17]:


ipl_df.info()


# In[18]:


#slicing
ipl_df[0:5]


# In[19]:


ipl_df['PLAYER NAME'][0:5]


# In[20]:


ipl_df[['PLAYER NAME','COUNTRY']][0:5]


# In[23]:


ipl_df.COUNTRY.value_counts()


# In[24]:


ipl_df.COUNTRY.value_counts(normalize = True) * 100


# In[28]:


# sorting dataframe by column values
ipl_df[['PLAYER NAME','SOLD PRICE']].sort_values('SOLD PRICE' )[0:5]


# In[29]:


# sorting dataframe by column values
ipl_df[['PLAYER NAME','SOLD PRICE']].sort_values('SOLD PRICE',ascending = False )[0:5]


# In[30]:


# create new columns
ipl_df['premium'] = ipl_df['SOLD PRICE'] - ipl_df['BASE PRICE']


# In[31]:


ipl_df[['PLAYER NAME','BASE PRICE','SOLD PRICE','premium']][0:5]


# In[32]:


ipl_df.groupby('AGE')['SOLD PRICE'].mean()


# In[36]:


# filtering records based on conditions
ipl_df[ipl_df['SIXERS'] > 80]


# In[37]:


ipl_df[ipl_df['SIXERS'] > 80][['PLAYER NAME','SIXERS']]


# In[38]:


# REMOing a column or row from a dataset
ipl_df.drop('Sl.NO.' , inplace = True , axis = 1)


# In[39]:


ipl_df


# In[40]:


ipl_df.columns


# In[48]:


ipl_df[ipl_df.AGE.isnull()]


# In[50]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[51]:


sn.barplot(x= 'AGE', y = 'SOLD PRICE', data = ipl_df)


# In[52]:


plt.hist(ipl_df['SOLD PRICE'])


# In[53]:


plt.hist(ipl_df['SOLD PRICE'] , bins = 20)


# In[57]:


sn.distplot(ipl_df['SOLD PRICE'])


# In[ ]:




