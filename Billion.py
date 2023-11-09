import streamlit as st
import pandas as pd
import seaborn as sns
import folium
from folium.plugins import HeatMap
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Load your dataset
df = pd.read_csv('Billionaires Dataset.csv')

# Check if 'category' and 'gender' columns exist in the dataset
if 'category' in df.columns and 'gender' in df.columns:
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to bottom, #0077b6, #00a5cf, #00c5af);
            color: white;
        }
        .st-cj {
            padding: 10px;
        }
        .st-eb {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
    st.dataframe(filtered_data, height=400)

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
