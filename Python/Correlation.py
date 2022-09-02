#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)


# In[3]:


df =pd.read_csv('E:/Projects/Portfolio Project/Python/archive/movies.csv')
df=df.dropna()


# In[4]:


df.head()


# In[6]:


for col in df.columns:
    pct_missing =np.mean(df[col].isnull())
    print('{} - {}%'.format(col, pct_missing))


# In[7]:


df.dtypes


# In[8]:


df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')


# In[9]:


df.head()


# In[10]:


df['yearcorrect'] = df['released'].str.extract(pat = '([0-9]{4})').astype(int)

df.head()


# In[53]:


df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[54]:


pd.set_option('display.max_rows', None)


# In[55]:


df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[56]:


df['company'].drop_duplicates().sort_values(ascending=False)


# In[57]:


df.drop_duplicates()


# In[60]:


plt.scatter(x=df['budget'],y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget')

plt.show()


# In[63]:


sns.regplot(x='budget', y='gross',data=df, scatter_kws={"color":"red"},line_kws={"color":"blue"})


# In[66]:


df.corr('pearson') #pearson method


# In[65]:


df.corr(method='kendall')


# In[67]:


df.corr(method='spearman')


# In[70]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix,annot=True)

plt.title('Correlation Matrix for Features')
plt.xlabel('Movies Features')
plt.ylabel('Budget')


# In[74]:


df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype =='object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes


# In[75]:


df_numerized


# In[79]:


correlation_matrix = df_numerized.corr()

sns.heatmap(correlation_matrix,annot=True)

plt.title('Correlation Matrix for Features')
plt.xlabel('Movies Features')
plt.ylabel('Movies Features')


# In[80]:


df_numerized.corr()


# In[82]:


correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs


# In[83]:


sorted_pairs = corr_pairs.sort_values()
sorted_pairs


# In[84]:


high_corr = sorted_pairs[(sorted_pairs)>.05]
high_corr


# In[ ]:


# Votes and Budget have the highest correlation to gross earnings

