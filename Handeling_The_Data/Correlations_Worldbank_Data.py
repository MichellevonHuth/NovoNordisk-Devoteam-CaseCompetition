#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import seaborn as sns


# In[63]:


df_obesity = pd.read_excel('Data/Overweight and Obesity Data.xlsx', 'BMI Children 2000-2016')

df_obesity.head()


# In[64]:


df_obesity = df_obesity[df_obesity['Obesity (Prevalence of BMI>2SD)'].notna()]
df_obesity_grouped = df_obesity.groupby(["Country"]).mean()

df_obesity_grouped


# In[65]:


df_education = pd.read_excel('Data/Data from Worldbank/WorldBank - Education Levels Enrolment (2000-2020).xlsx', 'Data')
df_education_grouped = df_education.groupby('Country Name').mean()
df_education_grouped['mean_education_2017-2020'] = df_education_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_education_grouped.rename(columns = {'2020':'education_2020'}, inplace = True)
df_education_selection = df_education_grouped[['mean_education_2017-2020', 'education_2020']]
df_education_selection


# In[66]:


df_sanitation = pd.read_excel('Data/Data from Worldbank/WorldBank - Sanitary Conditions (2000-2020).xlsx', 'Data')
df_sanitation_grouped = df_sanitation.groupby('Country Name').mean()
df_sanitation_grouped['mean_sanitation_2017-2020'] = df_sanitation_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_sanitation_grouped.rename(columns = {'2020':'sanitation_2020'}, inplace = True)
df_sanitation_selection = df_sanitation_grouped[['mean_sanitation_2017-2020', 'sanitation_2020']]
df_sanitation_selection


# In[67]:


df_diet = pd.read_excel('Data/Data from Worldbank/WorldBank - Healthy Diet Costs (2017-2020).xlsx', 'Data')

# focus on this category
df_diet = df_diet[df_diet['Category']=='Percent of the population who cannot afford a healthy diet at 52percentage of of income']
df_diet_grouped = df_diet.groupby('Country Name').mean()
df_diet_grouped['mean_diet_2017-2020'] = df_diet_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_diet_grouped.rename(columns = {'2020':'diet_2020'}, inplace = True)
df_diet_selection = df_diet_grouped[['mean_diet_2017-2020', 'diet_2020']]
df_diet_selection


# In[68]:


df_health = pd.read_excel('Data/Data from Worldbank/WorldBank - Health Related Data (2000, 2010, 2015, and 2019).xlsx', 'Data')

# focus on this category (only 2019 available)
df_tabacco = df_health[df_health['Category']=='Tobacco use - percentage of adults']
df_tabacco_grouped = df_tabacco.groupby('Country Name').mean()
df_tabacco_grouped.rename(columns = {'2019':'tabacco_2019'}, inplace = True)
df_tabacco_selection = df_tabacco_grouped[['tabacco_2019']]
df_tabacco_selection


# In[69]:


# alcohol (only 2015 available)
df_alcohol = df_health[df_health['Category']=='Alcohol consumption per capita - litres of pure alcohol']
df_alcohol_grouped = df_alcohol.groupby('Country Name').mean()
df_alcohol_grouped.rename(columns = {'2015':'alcohol_2015'}, inplace = True)

df_alcohol_selection = df_alcohol_grouped[['alcohol_2015']]
df_alcohol_selection


# In[70]:


df_health_expenditure = pd.read_excel('Data/Data from Worldbank/WorldBank - Health Expenditure (2000-2019).xlsx', 'Data')

# focus on this category
df_health_expenditure = df_health_expenditure[df_health_expenditure['Category']=='Health expenditure per capita  - US dollars']
df_health_expenditure_grouped = df_health_expenditure.groupby('Country Name').mean()
df_health_expenditure_grouped['mean_health_expenditure_2017-2019'] = df_health_expenditure_grouped[['2017', '2018', '2019']].mean(axis=1)
df_health_expenditure_grouped.rename(columns = {'2019':'health_expenditure_2019'}, inplace = True)
df_health_expenditure_selection = df_health_expenditure_grouped[['mean_health_expenditure_2017-2019', 'health_expenditure_2019']]
df_health_expenditure_selection
                                                                        


# In[71]:


df_gov_exp = pd.read_excel('Data/Data from Worldbank/WorldBank - Government Expenditure on Education (2000-2020).xlsx', 'Data')
df_gov_exp_grouped = df_gov_exp.groupby('Country Name').mean()
df_gov_exp_grouped['mean_gov_exp_2017-2020'] = df_gov_exp_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_gov_exp_grouped.rename(columns = {'2020':'gov_exp_2020'}, inplace = True)
df_gov_exp_selection = df_gov_exp_grouped[['mean_gov_exp_2017-2020', 'gov_exp_2020']]
df_gov_exp_selection


# In[72]:


df_food_cost = pd.read_excel('Data/Data from Worldbank/WorldBank - Food Costs (2017).xlsx', 'Data')

# focus on fruits and vegetables
df_food_cost = df_food_cost[(df_food_cost['Category']=='Cost of fruits') | (df_food_cost['Category']=='Cost of vegetables')]
df_food_cost_grouped = df_food_cost.groupby('Country Name').mean()
df_food_cost_grouped.rename(columns = {'2017':'fruit_veg_cost_2017'}, inplace = True)
df_food_cost_selection = df_food_cost_grouped[['fruit_veg_cost_2017']]
df_food_cost_selection


# In[73]:


df_bro_mobile = pd.read_excel('Data/Data from Worldbank/WorldBank - Broadband and Mobile Subscriptions (2000-2020).xlsx', 'Data')

# focus on this category
df_mobile = df_bro_mobile[df_bro_mobile['Category']=='Mobile subscriptions - per 100 people']
df_mobile_grouped = df_mobile.groupby('Country Name').mean()
df_mobile_grouped['mean_mobile_2017-2020'] = df_mobile_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_mobile_grouped.rename(columns = {'2020':'mobile_2020'}, inplace = True)
df_mobile_selection = df_mobile_grouped[['mean_mobile_2017-2020', 'mobile_2020']]

df_mobile_selection


# In[74]:


# broadband
df_broadband = df_bro_mobile[df_bro_mobile['Category']=='Broadband subscriptions - per 100 people']
df_broadband_grouped = df_broadband.groupby('Country Name').mean()
df_broadband_grouped['mean_broadband_2017-2020'] = df_broadband_grouped[['2017', '2018', '2019', '2020']].mean(axis=1)
df_broadband_grouped.rename(columns = {'2020':'broadband_2020'}, inplace = True)
df_broadband_selection = df_broadband_grouped[['mean_broadband_2017-2020', 'broadband_2020']]
df_broadband_selection


# In[75]:


df_obesity_grouped = df_obesity_grouped.merge(df_education_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_sanitation_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_diet_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_tabacco_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_alcohol_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_health_expenditure_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_gov_exp_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_food_cost_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_mobile_selection, how='left', left_index=True, right_index=True)
df_obesity_grouped = df_obesity_grouped.merge(df_broadband_selection, how='left', left_index=True, right_index=True)


# In[76]:


df_obesity_grouped


# In[77]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_education_2017-2020')


# In[78]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_sanitation_2017-2020')


# In[79]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_diet_2017-2020')


# In[80]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='tabacco_2019')


# In[81]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='alcohol_2015')


# In[82]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_health_expenditure_2017-2019')


# In[83]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_gov_exp_2017-2020')


# In[84]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='fruit_veg_cost_2017')


# In[85]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_mobile_2017-2020')


# In[86]:


sns.regplot(data=df_obesity_grouped, x='Obesity (Prevalence of BMI>2SD)', y='mean_broadband_2017-2020')


# In[87]:


df_obesity_grouped.describe()


# In[88]:


df_obesity_grouped


# In[89]:


df_obesity_grouped[df_obesity_grouped.index=='Malaysia']


# In[90]:


df_obesity_grouped_filtered = df_obesity_grouped[df_obesity_grouped.index.isin(['Kuwait', 'United States', 'Puerto Rico', 'Qatar', 'Egypt', 'Bahrain', 'Saudi Arabia', 'United Arab Emirates', 'New Zealand', 'Chile', 'Dominican Republic', 'Mexico','Oman', 'Lebanon', 'Libya', 'Iraq', 'Venezuela', 'Uruguay', 'Greece','Jamaica', 'Algeria', 'Malaysia', 'Jordan', 'Italy'])]



# In[91]:


df_obesity_grouped_filtered.describe()


# In[92]:


df_obesity_grouped_filtered.sort_values('mobile_2020', ascending=False)['mobile_2020']

