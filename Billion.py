import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
from wordcloud import WordCloud

# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Check if 'category' and 'gender' columns exist in the dataset
if 'category' in df.columns and 'gender' in df.columns:
    # Title for the dashboard
    st.title('Mugare List of Billionaires Dashboard')

    # Sidebar for user input
    st.sidebar.header('Filter Data')
    selected_category = st.sidebar.selectbox('Select Category', df['category'].unique())
    selected_gender = st.sidebar.selectbox('Select Gender', df['gender'].unique())

    # Filter the data based on user selection
    filtered_data = df[(df['category'] == selected_category) & (df['gender'] == selected_gender)]

    # Display a bar chart of the filtered data
    st.subheader('Distribution of Billionaires by Age in the Selected Category and Gender')
    age_counts = filtered_data['age'].value_counts()
    st.bar_chart(age_counts)

    # Display a scatter plot of 'finalWorth' vs. 'age' for the filtered data
    st.subheader('Final Worth vs. Age for the Selected Category and Gender')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=filtered_data, x='age', y='finalWorth', ax=ax)
    st.pyplot(fig)

    # Display a table of the filtered data
    st.subheader('Table of Billionaires')
    st.write(filtered_data)

    # Additional charts
    # 1. Histogram of Wealth Distribution
    st.subheader('Wealth Distribution for the Selected Category and Gender')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=filtered_data, x='finalWorth', bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    # 2. Box Plot of Wealth by Category
    st.subheader('Wealth Distribution by Category')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=filtered_data, x='category', y='finalWorth', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # 3. Pair Plot for Multivariate Analysis
    st.subheader('Pair Plot for Multivariate Analysis')
    st.pyplot(sns.pairplot(filtered_data, hue='category', markers=["o", "s", "D"]))



    # 5. Correlation Heatmap (if you have numeric columns)
    st.subheader('Correlation Heatmap')
    fig, ax = plt.subplots(figsize=(10, 8))
    correlation_matrix = filtered_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # 6. Geospatial Heatmap for Location Density
    st.subheader('Geospatial Heatmap of Billionaire Locations')
    locations = filtered_data[['latitude_country', 'longitude_country']].values
    m = folium.Map(location=[filtered_data['latitude_country'].mean(), filtered_data['longitude_country'].mean()], zoom_start=5)
    HeatMap(locations).add_to(m)
    st.map(m)

    # 7. Word Cloud for Popular Names or Keywords (if you have a 'personName' or 'keywords' column)
    st.subheader('Word Cloud for Popular Names or Keywords')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_data['personName']))
    st.image(wordcloud.to_array(), use_container_width=True)

    # Add a pie chart to show the distribution of categories for the selected gender
    st.subheader('Distribution of Categories for the Selected Gender')
    category_counts = filtered_data['category'].value_counts()
    st.pyplot(plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140))

# End the Streamlit app
st.stop()
