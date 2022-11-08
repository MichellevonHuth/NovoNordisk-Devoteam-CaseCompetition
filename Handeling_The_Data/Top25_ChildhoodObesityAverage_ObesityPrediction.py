#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import seaborn as sns

# Extracting Overweight and Obesity Data
df2 = pd.read_excel('Overweight and Obesity Data.xlsx', sheet_name='BMI Children 2000-2016') 
bmi_kids = df2
bmi_kids.drop_duplicates(inplace=True)
bmi_kids = bmi_kids[bmi_kids['Year'] == 2016]
bmi_kids = bmi_kids.groupby('Country').mean()
print(bmi_kids.nlargest(10, 'Overweight (Prevalence of BMI>1SD)'))

# Extracting Population Data
pop = pd.read_excel('./Data from Worldbank/WorldBank - Population Data (2000-2020).xlsx', sheet_name='Data') 
pop.drop_duplicates(inplace=True)
pop.dropna(inplace=True)
pop = pop[(pop.Category == "Urban population") | (pop.Category == "Rural population")]
pop = pop.groupby('Country Name').sum()
print(pop.nlargest(10, '2016'))

# Join obesity data and population data
pop = pop.rename(columns={"Country Name": "Country"})
result = pd.concat([bmi_kids, pop], axis=1, join="inner")
result = result.sort_values(by=['2016'], ascending=False)

# Filter countries with population over 1 mio people and sort by Obesity
result = result[result["2016"] > 1000000]
result = result.sort_values(by=['Obesity (Prevalence of BMI>2SD)'], ascending=False)
print(result.head())
result.head(25).to_csv('top25.csv', index=True)

# Import obesity prediction data
df = pd.read_excel('Overweight and Obesity Data.xlsx', sheet_name='Obesity pred Children 2016 & 20')
pred_kids = df
pred_kids.drop_duplicates(inplace=True)

# Import extraction data
top25 = pd.read_csv("top25.csv")

# Prediction data only for top25 countries
pred = pred_kids[pred_kids["Country"].isin(list(top25["Unnamed: 0"].unique()))]
top25 = top25.rename(columns={"Unnamed: 0": "Country"})
pred2 = pred.drop(df.columns[[4, 5, 6,7]],axis = 1)
pred3 = top25.merge(pred2, how='inner', on='Country')
print(pred3.head())

# Combine childhood obesity values by creating an average
pred3["Predicted 2030:  % children with obesity"] = pred3.apply(lambda x: (x["Predicted 2030: % children aged 5-9 with obesity"] + x["Predicted 2030: % children aged 10-19 with obesity"])/2, axis=1)
pred3.sort_values(by=['Predicted 2030: % children with obesity'], ascending=False)

# Strip dataset for important columns
pred4 = pred3.drop(pred3.columns[[5,6, 8, 9, 10, 11]],axis = 1)
pred4.sort_values(by=['Predicted 2030: % children with obesity'], ascending=False)
pred4.to_csv('childhood_growth.csv', index=True)

# Combine historical and prediction data
df2 = pd.read_excel('Overweight and Obesity Data.xlsx', sheet_name='BMI Children 2000-2016') 
bmi_kids = df2
bmi_kids.drop_duplicates(inplace=True)
bmi_kids = bmi_kids[bmi_kids['Country'] == "Malaysia"]
bmi_kids.dropna(inplace=True)

# Drop unnecessary features
bmi_kids2 = bmi_kids.drop(bmi_kids.columns[[1,4,6,7,8]],axis = 1)

# Group the age groups of Children in Obesity data
bmi_kids2.groupby(by=["Country", "Year", "Age group"],as_index=False).sum()
bmi_kids2["Obesity (Prevalence of BMI>2SD)"] = bmi_kids2["Obesity (Prevalence of BMI>2SD)"]/2
bmi_kids59 = bmi_kids2[(bmi_kids["Age group"] <= 9)]
bmi_kids59 = bmi_kids59.groupby(by=["Country", "Year"], as_index=False).sum()
bmi_kids59["Obesity (Prevalence of BMI>2SD)"] = bmi_kids59["Obesity (Prevalence of BMI>2SD)"]/5
bmi_kids59["Age group"] = "5-9"
bmi_kids1019 = bmi_kids2[(bmi_kids["Age group"] > 9)]
bmi_kids1019 = bmi_kids1019.groupby(by=["Country", "Year"],as_index=False).sum()
bmi_kids1019["Obesity (Prevalence of BMI>2SD)"] = bmi_kids1019["Obesity (Prevalence of BMI>2SD)"]/10
bmi_kids1019["Age group"] = "10-19"


# Obesity prediction for Malaysia
df = pd.read_excel('Overweight and Obesity Data.xlsx', sheet_name='Obesity pred Children 2016 & 20') 
pred_kids = df
pred_kids.drop_duplicates(inplace=True)
pred_kids.dropna(inplace=True)
pred_kids = pred_kids[pred_kids['Country'] == "Malaysia"]
pred_kids2 = pred_kids.copy()
pred_kids3 = pd.concat([pred_kids, pred_kids2])
pred_kids4 = pred_kids3.drop(pred_kids3.columns[[1,2,3,4,5,6, 7, 10,11]],axis = 1)
pred_kids4["Age group"] = ["5-9", "10-19"]
pred_kids4["Obesity (Prevalence of BMI>2SD)"] = [0.249, 0.2]
pred_kids4 = pred_kids4.drop(pred_kids4.columns[[1,2]],axis = 1)
pred_kids4["Year"] = 2030

# Merge Obesity historical data and prediction data
df = pd.concat([bmi_kids59, bmi_kids1019, pred_kids4])
df["Prognose"] = False
df.iloc[34,4] = True
df.iloc[35,4] = True
df.to_csv('linechart.csv', index=True)

