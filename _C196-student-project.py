#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Name: ")
print("Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population")
print("Show a comparison between Meat and Vegetables consumption across the countries")


# In[2]:


#predefine code for image
from IPython.display import Image
Image(filename='healthy.jpg') 
#predefine code end


# # Activity - 1 Clean the data and show which top 10 countries has the highest Undernourished rate as compared with their Population

# In[4]:


#import the required packages 
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file.
df = pd.read_csv("COVID-19 Healthy Diet Dataset.csv")
df

df.replace("<2.5", int(3), inplace=True) 
df

df['Undernourished'] = df['Undernourished'].astype(float)
df

gc = df.groupby('Country')[['Undernourished','Population']].sum().reset_index()
gc

su = gc.sort_values(by = ['Undernourished'],ascending = False)
su

tp10 = su.head(10)
tp10['percentage_number'] = tp10['Undernourished']/100*tp10['Population']
tp10

tp = tp10['Population']
pn = tp10['percentage_number']

i = tp10['Country']
plt.subplots(figsize = (10,8))

plt.title('Pla ten Contrie',fontsize = 20)
plt.bar(i,tp,bottom = pn,color = 'green',label = 'Country Population')
plt.bar(i,pn,color = 'red',label = 'Undernourished')
plt.xticks(rotation = 80)
plt.legend()
plt.xlabel("Country")
plt.ylabel("Population")
plt.show()


# In[ ]:





# In[ ]:


#Converting object datatype column to float datatype


# In[ ]:


#Groupby country and apply sum on Undernourished and Population column and create a new dataframe out of it


# In[ ]:


#Sort the new dataframe as per Undernourished column


# In[ ]:


#Get the top 10 countries from the sorted data


#Convert Undernourished percentage to number and add a new column to the top 10 countries dataframe


# In[ ]:


#Plot a stacked bar graph for showing the Population vs Undernourished rate


# Conclusion - 

# # Activity - 2 Show a comparison between Meat and Vegetables consumption across the countries

# In[ ]:


#Sort the big dataframe as per Meat consumption


# In[ ]:


#Sort the big dataframe as per Vegetables consumption


# In[ ]:


#Plot a histogram showing the Meat consumption vs Vegetables consumption across countries 


# Conclusion - 

# In[ ]:




