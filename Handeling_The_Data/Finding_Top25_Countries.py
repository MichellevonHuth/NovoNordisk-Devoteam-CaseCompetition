#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


path_to_files = "/Users/davidbellenberg/Desktop/Case_Competition_2022/Data/"
df_all = pd.read_excel(path_to_files +"Overweight and Obesity Data.xlsx",sheet_name="BMI Children 2000-2016")


# In[ ]:


#drop all entries without data about 
df_all_dropped = df_all[df_all['Obesity (Prevalence of BMI>2SD)'].notna()]

df_all_dropped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")


# In[ ]:


#filter by year
df_all_dropped = df_all[df_all['Obesity (Prevalence of BMI>2SD)'].notna()]

df_all_dropped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")

df_all_dropped_year = df_all_dropped[df_all_dropped["Year"]==2016]

df_grouped = df_all_dropped_year.groupby(["Country"]).mean()

df_grouped_largest = df_grouped.nlargest(n=10, columns="Obesity (Prevalence of BMI>2SD)")

df_grouped_largest["Obesity (Prevalence of BMI>2SD)"]





# In[4]:


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

joined_cutat_20mio.nlargest(n=25, columns="Obesity (Prevalence of BMI>2SD)")


# In[ ]:


sns.scatterplot(data=joined_cutat_20mio,x="2016", y="Obesity (Prevalence of BMI>2SD)")


# In[ ]:




