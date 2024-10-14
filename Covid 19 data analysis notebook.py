#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# ### Let's Import the modules 

# In[125]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[89]:


corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[90]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[91]:


corona_dataset_csv.drop(["Lat","Long"], axis =1, inplace = True)


# In[92]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[93]:


corona_dataset_aggregated= corona_dataset_csv.groupby("Country/Region").sum()


# In[94]:


corona_dataset_aggregated.head()


# In[95]:


corona_dataset_aggregated.shape
#187 countries/rows, and 100 columns or time periods


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[96]:


corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()

plt.legend()


# In[97]:


corona_dataset_aggregated.loc['China'].plot()


# In[98]:


corona_dataset_aggregated.loc["China"][:3].plot()
#beginning first 3 days in china


# ### task 3.1: caculating the first derivative of the curve

# In[99]:


corona_dataset_aggregated.loc["China"].diff().plot()


# ### task 3.2: find maxmimum infection rate for China

# In[100]:


corona_dataset_aggregated.loc["China"].diff().max()
# find maxmimum infection rate for China


# In[101]:


corona_dataset_aggregated.loc["Italy"].diff().max()


# In[102]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[103]:


countries = list (corona_dataset_aggregated.index)
max_infection_rates = []

for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates

corona_dataset_aggregated["max_infection_rate"]=max_infection_rates


# In[104]:


corona_dataset_aggregated.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[105]:


corona_data =pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[106]:


corona_data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[107]:


happiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[108]:


happiness_report_csv.head()


# ### Task 4.2: let's drop the useless columns 

# In[109]:


useless_cols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]


# In[110]:


happiness_report_csv.drop(useless_cols, axis =1, inplace=True)
happiness_report_csv.head()


# ### Task 4.3: changing the indices of the dataframe

# In[111]:


happiness_report_csv.set_index("Country or region", inplace=True)
happiness_report_csv.head()


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# #### wolrd happiness report Dataset :

# In[112]:


corona_data.head()


# In[113]:


corona_data.shape


# In[114]:


happiness_report_csv.head()


# In[115]:


happiness_report_csv.shape


# In[116]:


data=corona_data.join(happiness_report_csv, how ="inner")
data.head()


# ### Task 4.5: correlation matrix 

# In[117]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[127]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[135]:


x= data["GDP per capita"]
y= data["max_infection_rate"]
sns.scatterplot(x=x,y=np.log(y))


# In[136]:


sns.regplot(x=x,y=np.log(y))


# 

# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[142]:


data.head()


# In[145]:


x= data["Social support"]
y= data["max_infection_rate"]
sns.scatterplot(x=x,y=np.log(y))


# In[146]:


sns.regplot(x=x,y=np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[149]:


x= data["Healthy life expectancy"]
y= data["max_infection_rate"]
sns.scatterplot(x=x,y=np.log(y))


# In[150]:


sns.regplot(x=x,y=np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[151]:


x=data["Freedom to make life choices"]
y=data["max_infection_rate"]
sns.scatterplot(x=x,y=np.log(y))


# In[152]:


sns.regplot(x=x,y=np.log(y))


# In[ ]:




