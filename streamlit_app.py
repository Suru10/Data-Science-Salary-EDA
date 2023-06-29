#import libraries
import streamlit as st
import pandas as pd
import warnings
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

warnings.filterwarnings("ignore")
df = pd.read_csv('ds_salaries.csv')
#Introduction
st.subheader('Whimsical Wolves ')
st.write(' Hello, my name is Jamie, I am in 7th grade and I have learned how to code in the past 5 days')
st.write('Hello, my name is Joshua, I am in 10th grade and I ')
#Title
st.title('Data Science Salaries 2023 EDA')
# Inspection:
st.subheader('Inspectionm')

# Code for Inspection:
df.head()
df.tail()
df.describe()
df.columns
df.shape
df['experience_level'].unique()
df['experience_level'].value_counts()
df.isna().sum()

# Code for Cleaning:
#Drop Code
columns_to_drop = ['salary', 'salary_currency', 'employment_type']
df.drop(columns_to_drop, axis=1, inplace=True)
#Value Name Change
df['experience_level'] = df['experience_level'].replace(
  'SE', 'Senior Executive')
df['experience_level'] = df['experience_level'].replace('MI', 'Middle Level')
df['experience_level'] = df['experience_level'].replace('EX', 'Executive')
df['experience_level'] = df['experience_level'].replace('EN', 'Entry Level')

# Change country codes to names
country_mapping = {
  'ES': 'Spain',
  'US': 'United States',
  'CA': 'Canada',
  'DE': 'Germany',
  'GB': 'United Kingdom',
  'NG': 'Nigeria',
  'IN': 'India',
  'HK': 'Hong Kong',
  'PT': 'Portugal',
  'NL': 'Netherlands',
  'CH': 'Switzerland',
  'CF': 'Central African Republic',
  'FR': 'France',
  'AU': 'Australia',
  'FI': 'Finland',
  'UA': 'Ukraine',
  'IE': 'Ireland',
  'IL': 'Israel',
  'GH': 'Ghana',
  'AT': 'Austria',
  'CO': 'Colombia',
  'SG': 'Singapore',
  'SE': 'Sweden',
  'SI': 'Slovenia',
  'MX': 'Mexico',
  'UZ': 'Uzbekistan',
  'BR': 'Brazil',
  'TH': 'Thailand',
  'HR': 'Croatia',
  'PL': 'Poland',
  'KW': 'Kuwait',
  'VN': 'Vietnam',
  'CY': 'Cyprus',
  'AR': 'Argentina',
  'AM': 'Armenia',
  'BA': 'Bosnia and Herzegovina',
  'KE': 'Kenya',
  'GR': 'Greece',
  'MK': 'North Macedonia',
  'LV': 'Latvia',
  'RO': 'Romania',
  'PK': 'Pakistan',
  'IT': 'Italy',
  'MA': 'Morocco',
  'LT': 'Lithuania',
  'BE': 'Belgium',
  'AS': 'American Samoa',
  'IR': 'Iran',
  'HU': 'Hungary',
  'SK': 'Slovakia',
  'CN': 'China',
  'CZ': 'Czech Republic',
  'CR': 'Costa Rica',
  'TR': 'Turkey',
  'CL': 'Chile',
  'PR': 'Puerto Rico',
  'DK': 'Denmark',
  'BO': 'Bolivia',
  'PH': 'Philippines',
  'DO': 'Dominican Republic',
  'EG': 'Egypt',
  'ID': 'Indonesia',
  'AE': 'United Arab Emirates',
  'MY': 'Malaysia',
  'JP': 'Japan',
  'EE': 'Estonia',
  'HN': 'Honduras',
  'TN': 'Tunisia',
  'RU': 'Russia',
  'DZ': 'Algeria',
  'IQ': 'Iraq',
  'BG': 'Bulgaria',
  'JE': 'Jersey',
  'RS': 'Serbia',
  'NZ': 'New Zealand',
  'MD': 'Moldova',
  'LU': 'Luxembourg',
  'MT': 'Malta'
}
df['employee_residence'] = df['employee_residence'].replace(country_mapping)

# Visualizations:

# Hypothesis 1: Which job title, for data science, on average has the highest salary? Joshua
# Insert code here
st.title('Hypothesis 1')
average_job_title_salary = df.groupby(
  'job_title')['salary_in_usd'].mean().reset_index()
g = sns.barplot(average_job_title_salary, x='job_title', y='salary_in_usd')
plt.title('Average Salary Based on Job Title')
plt.xticks(rotation=90)
sns.set(rc={'figure.figsize': (15, 5)})
plt.xlabel("sepal_length", fontsize=2)
plt.show()

st.write('This bar graph shows the average salary of a data scientists based off their job title.')
st.
# Summary of graph

# This bar graph shows the average salary of a data scientists based off their job title. This graph is very straghtforward and it is clear that there is a big wage gap between job titles.

# Hypothesis 2: How much does a data scientist’s experience level affect their salary? Joshua

# Insert code here
sns.violinplot(df, x="experience_level", y="salary_in_usd")
plt.title('Average Salary Based on Experience Level')
plt.show()
#Summary of graph

# This graph shows the distribution of salaries based off experience level.
# The thicker the violin graph gets the more people are in that salary range.
# In this case for example, most entry level data scientists hover around
# 75k per year.

#Hypothesis 3: How does the country of residence affect a data scientist’s salary?-Jamie
# Insert code here
Hypothesis_3 = df.groupby(
  "employee_residence")['salary_in_usd'].mean().reset_index()
fig = px.bar(
  x=Hypothesis_3["employee_residence"],
  y=Hypothesis_3['salary_in_usd'],
)
fig.show()
# Ctrl + /
# command + /
#Trends in Graph
#  Overall, most of the countries make the same amount for the amount of data scientist they have. although, based on the data the countries with more data sciencetist generally make more than the countiries with less data scientist. the only outlier data point is israel, they make over 400k, with only having one Data scientist.

# Hypothesis 4: How does the amount of remote work affect a data science  salary in usd? -Jamie
# Insert code here
Hypothesis_4 = df.groupby("remote_ratio")['salary_in_usd'].mean().reset_index()
fig = px.pie(Hypothesis_4,
             values='salary_in_usd',
             names='remote_ratio',
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()

# Trends in the Graph
#   The Data scientist that work 0% remote make the most with an average salary of around 144k.
#   The Data scientist that work 50% remote make the least with an average salary of 80k.
#   The Data scientist that work 100% remote make an average salary of 135k.

#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
# st.title("Title Here")

# #adding discription to your website
# st.text('Description')

# #Thesis here
# st.header('Thesis')
# st.text('Add your Thesis here')

# #SHOWING THE DATA
# #dataset Header
# st.header('Dataset')

# #add your dataset (delete dataset this is an example)
# BostonHousing = pd.read_csv("BostonHousing.csv")

# #showing dataset
# st.table(BostonHousing.head())
# st.text('Showing dataset and writting about it here')

# #Adding images to make your streamlit look visually better!
# st.image('pro.png')
# st.text('You can add photos with descriptions')

# #Adding 3-6 Visualizations using photos collected and made from your graph
# #adding images
# #adding graphs by images
# st.image('pasted image 0.png')
# st.text('Discription about your graph and visualizations')

# #adding graphs by making plotly_Chart
# # Plot!
# #st.plotly_chart(BostonHousing, use_container_width=True)
# #st.text('Discription')

# #adding conclusions
# # st.header('Conclusion')
# # st.text('add your conclusion here')
