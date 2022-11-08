#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

 

from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


# In[7]:


df_all = pd.read_excel('Overweight and Obesity Data.xlsx', 'BMI Children 2000-2016')


# In[8]:


#drop all entries without data about 
df_all_dropped = df_all[df_all['Obesity (Prevalence of BMI>2SD)'].notna()]

df_all_dropped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")


# In[9]:


#filter by year
df_all_dropped = df_all[df_all['Obesity (Prevalence of BMI>2SD)'].notna()]

df_all_dropped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")

df_all_dropped_year = df_all_dropped[df_all_dropped["Year"]==2016]

df_grouped = df_all_dropped_year.groupby(["Country"]).mean()

df_grouped_largest = df_grouped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")

df_grouped_largest["Obesity (Prevalence of BMI>2SD)"]





# In[24]:


#import population data
df_pop = pd.read_excel(path_to_files +"WorldBank_Population Data_(2000-2020).xlsx",sheet_name="Data")

#drop null values
df_pop = df_pop[df_pop['2016'].notna()]

df_pop_year = df_pop[["Country Name","2016","Category"]]

df_pop_year_urban = df_pop_year.loc[(df_pop_year['Category'] == "Urban population") | (df_pop_year['Category'] == "Rural population")]

df_pop_year_urban_grouped = df_pop_year_urban.groupby(["Country Name"]).sum()


#join dataframes


joined = pd.merge(df_grouped, df_pop_year_urban_grouped,  how='left', left_index=True, right_index=True)


joined_cutat_20mio = joined[joined["2016"] > 1000000]

joined_cutat_20mio.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")


# # Broadband and Mobile Subscriptions 

# In[58]:


df_mobile = pd.read_excel('WorldBank - Broadband and Mobile Subscriptions (2000-2020).xlsx', 'Data')


# In[59]:


df_mobile.head()


# In[88]:


df_mobile_grouped = df_mobile.groupby(['Country Name']).mean()
df_mobile_grouped


# In[89]:


df_mobile_cleaned = df_mobile_grouped.dropna()
df_mobile_cleaned.head()


# In[99]:


df_main_dataset


# In[104]:


df_mobile_joined = pd.merge(df_main_dataset, df_mobile_cleaned,  how='left', left_index=True, right_index=True)


# In[105]:


df_mobile_joined.head()


# In[108]:


df_mobile_joined['mean'] = df_mobile_joined[['2017', '2018', '2019', '2020']].mean(axis=1)
df_mobile_joined[['mean', '2016', '2017', '2018', '2019', '2020']].sort_values('mean', ascending=False)


# In[111]:


df_mobile_joined.to_csv('/Users/michellevonhuth/Desktop/Case Competition 2022/' + "mobile.csv")


# In[110]:


df_mobile_joined.plot.scatter(x='mean', y='Obesity (Prevalence of BMI>2SD)')


# In[ ]:




