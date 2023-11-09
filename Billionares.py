#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import matplotlib.pyplot as plt


# In[61]:


# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')


# In[62]:


df.head


# In[63]:


plt.scatter(df['age'], df['finalWorth'])
plt.xlabel('Age')
plt.ylabel('Final Worth')
plt.title('Scatter Plot of Age vs Final Worth')
plt.show()


# # Bar Chart:To compare the distribution of "categories."
# 
# 

# In[64]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Distribution of Categories')
plt.xticks(rotation=45)
plt.show()


# # Histogram:To visualize the distribution of "age."

# In[65]:


import matplotlib.pyplot as plt

plt.hist(df['age'], bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()


# # Line Chart:To show the trend of "finalWorth" over "birthYear."

# In[66]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=df, x='birthYear', y='finalWorth')
plt.xlabel('Birth Year')
plt.ylabel('Final Worth')
plt.title('Final Worth over Birth Year')
plt.show()


# # Box Plot:To visualize the distribution of "finalWorth" by "gender."

# In[67]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df, x='gender', y='finalWorth')
plt.xlabel('Gender')
plt.ylabel('Final Worth')
plt.title('Final Worth Distribution by Gender')
plt.show()


# # Create Pie Chart to Show which industry is big

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Count the frequency of each category
category_counts = df['category'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories')

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
plt.show()


# # bar chart that visualizes the count of billionaires in each country

# In[69]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Count the number of billionaires in each country
country_counts = df['country'].value_counts()

# Sort the countries by the number of billionaires (optional)
country_counts = country_counts.sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
plt.bar(country_counts.index, country_counts.values)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.xlabel('Country')
plt.ylabel('Number of Billionaires')
plt.title('Number of Billionaires by Country')

# Show the bar chart
plt.tight_layout()  # Ensures that labels are not cut off in the saved image
plt.show()


# # Time Series Line Chart - Change in "finalWorth" over time:

# In[70]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Convert the date column to datetime if needed
df['date'] = pd.to_datetime(df['date'])

# Group by year and calculate the mean finalWorth for each year
finalWorth_by_year = df.groupby(df['date'].dt.year)['finalWorth'].mean()

# Create a time series line chart
plt.figure(figsize=(10, 5))
plt.plot(finalWorth_by_year.index, finalWorth_by_year.values)
plt.xlabel('Year')
plt.ylabel('Mean Final Worth')
plt.title('Mean Final Worth Over Time')
plt.grid(True)
plt.show()


# # Stacked Bar Chart - Distribution of "categories" by "gender":
# 
# 

# In[71]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Create a pivot table to count categories by gender
pivot_table = df.pivot_table(index='category', columns='gender', values='personName', aggfunc='count')

# Create a stacked bar chart
pivot_table.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Distribution of Categories by Gender')
plt.legend(title='Gender', loc='upper right')
plt.show()


# # Treemap: Visualize hierarchical data, such as the distribution of "categories" and "industries" within "country."

# In[72]:


import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Group data by 'country', 'category', and 'industries' to count occurrences
grouped_data = df.groupby(['country', 'category', 'industries']).size().reset_index(name='count')

# Create a treemap chart
fig = px.treemap(grouped_data, path=['country', 'category', 'industries'], values='count',
                 title='Hierarchical Distribution of Categories and Industries by Country')

# Show the interactive treemap chart
fig.show()


# In[ ]:





# In[ ]:




