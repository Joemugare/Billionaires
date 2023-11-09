import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page title and layout as the first Streamlit command
st.set_page_config(page_title='Streamlit Dashboard', layout='wide')

# Set the title as the header
st.title("Mugare's Billionaire Dashboard")

# Load your dataset with specified encoding
df = pd.read_csv('Billionaires Dataset.csv', encoding='latin-1')

# Create a sidebar
sidebar = st.sidebar

# Add a header to the sidebar
sidebar.header('Filters')

# Check if the 'age' column exists in your DataFrame
if 'age' in df.columns:
    # Add a selectbox to the sidebar
    category_selectbox = sidebar.selectbox('Select Category:', df['category'].unique())

    # Add a slider to the sidebar for age
    age_slider = sidebar.slider('Select Age Range:', int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))

    # Filter the data based on the sidebar selections
    filtered_df = df[df['category'] == category_selectbox]

    # Filter the DataFrame using boolean indexing for the age range
    filtered_df = filtered_df[(filtered_df['age'] >= age_slider[0]) & (filtered_df['age'] <= age_slider[1])]

    # Create a main layout for filtered data
    filtered_data_layout = st.container()

    # Create a line chart with example columns (modify as needed)
    line_chart_filtered = px.line(filtered_df, x='birthYear', y='finalWorth', color='personName')

    # Add the filtered line chart to the filtered data layout
    filtered_data_layout.plotly_chart(line_chart_filtered)

    # Display the filtered DataFrame
    st.write("Filtered Data:", filtered_df)
else:
    st.warning("The 'age' column does not exist in the dataset.")

# Create a main layout for the original data
main_layout = st.container()

# Create a line chart with example columns (modify as needed)
line_chart = px.line(df, x='birthYear', y='finalWorth', color='personName')

# Add the original line chart to the main layout
main_layout.plotly_chart(line_chart)

# Create a bar chart showing the distribution of finalWorth by country
bar_chart = px.bar(df, x='country', y='finalWorth')

# Add the bar chart to the main layout
main_layout.plotly_chart(bar_chart)

# Create a pie chart showing the distribution of people by industry
pie_chart = px.pie(df, values='finalWorth', names='industries')

# Add the pie chart to the main layout
main_layout.plotly_chart(pie_chart)

# Add a download button to allow users to download the data as a CSV file
st.download_button('Download Data', df.to_csv(), file_name='data.csv')
