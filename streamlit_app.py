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
# Introduction
st.subheader('Whimsical Wolves ')
st.write(
  ' Hello, my name is Jamie, I am in 7th grade and I have learned how to code in the past 5 days'
)
st.write(
  "Hello, my name is Joshua, I am in 10th grade and I've been coding for the last 4 years. I've learned languages such as python, java, and SQL."
)
# Title
st.title('Data Science Salaries 2023 EDA')
st.write(
  'This data set is comprised of information about jobs related to analyzing data and how it affects their salary. The data set was updated 3 months ago. The Data has been sourced from aijobs.net.'
)
st.markdown("""---""")

# Inspection:
#exampple of the data
st.header('Inspection:')
st.write(" This is an example of what our data looks like:")
st.write("\n")
st.write(df.head())
st.write( 'The experience level and The employee residence columns have values that  ')

col1, col2 = st.columns(2)
col1.write(df.isna().sum())
col2.write(
  "According to the graph there is no null values, that's good because it keeps the data consistent."
)

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
st.title('The Organized Data')
st.subheader(
  'Hypothesis 1: Which job titles, for data science, on average have the highest paying salaries?'
)
average_job_title_salary = df.groupby(
  'job_title')['salary_in_usd'].mean().reset_index()

fig = px.bar(average_job_title_salary, x='job_title', y='salary_in_usd')
fig.update_layout(title='Average Salary Based on Job Title',
                  xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

st.write(
  'This bar graph shows the average salary of a data scientists based off their job title.'
)
st.markdown("""---""")
st.write("Salaries range from as low as 5,400$ per year to as high as 375,000")
st.markdown("""---""")
st.write(
  "The highest paying job titles on average are Data Science Tech lead, Cloud Data Architect, and Data Lead"
)
# Summary of graph

# This bar graph shows the average salary of a data scientists based off their job title. This graph is very straghtforward and it is clear that there is a big wage gap between job titles.

# Hypothesis 2: How much does a data scientist’s experience level affect their salary? Joshua

# Insert code here
st.subheader(
  "Hypthesis 2: How much does a data scientist's experience level affect their salary?"
)

fig, ax = plt.subplots()
violin = sns.violinplot(data=df,
                        x="experience_level",
                        y="salary_in_usd",
                        ax=ax)
# violin = sns.violinplot(df, x="experience_level", y="salary_in_usd")
plt.title('Average Salary Based on Experience Level')
fig = violin.get_figure()
st.pyplot(fig)

# violin = sns.violinplot(df, x="experience_level", y="salary_in_usd")
# plt.title('Average Salary Based on Experience Level')
# # plt.show()
# # st.pyplot(violin)
# st.pyplot(fig)
#Summary of graph

st.write(
  "This graph shows the distribution of salaries based off experience level. The thicker the violin graph gets the more people are in that salary range."
)
st.markdown("""---""")
st.write(
  "There is a clear gap between experience levels with entry level data scientists only averaging 75k per year while senior executives average almost 200k per year."
)

# The thicker the violin graph gets the more people are in that salary range.
# , most entry level data scientists hover around
# 75k per year.

#Hypothesis 3: How does the country of residence affect a data scientist’s salary?-Jamie
# Insert code here
st.subheader(
  "Hypthesis 3: How does the country of residence affect a data scientist’s salary?"
)
Hypothesis_3 = df.groupby(
  "employee_residence")['salary_in_usd'].mean().reset_index()
fig = px.bar(
  x=Hypothesis_3["employee_residence"],
  y=Hypothesis_3['salary_in_usd'],
)
st.plotly_chart(fig, use_container_width=True)
# Ctrl + /
# command + /
#Trends in Graph
st.write(
  "Overall, most of the countries make the same amount of data scientists, although, the countries with more data scientist generally make more than the countiries with less data scientist."
)
st.markdown("""---""")
st.write(
  "The only outlier data point is israel, they make over 400k, with only having one Data scientist."
)

# Hypothesis 4: How does the amount of remote work affect a data science  salary in usd? -Jamie
# Insert code here
st.subheader(
  "Hypthesis 4: Does the amount of remote work a data scientists has affect their average salary?"
)
Hypothesis_4 = df.groupby("remote_ratio")['salary_in_usd'].mean().reset_index()
fig = px.pie(Hypothesis_4,
             values='salary_in_usd',
             names='remote_ratio',
             color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig, use_container_width=True)

# Trends in the Graph
st.write(
  "The information from the graph above shows that data scientists who do none of their work remote tend to make significantly more than data scientists who do 50% remote work."
)
st.markdown("""---""")
st.write("Data scientists who only do remote work actually average a salary of 135k per year which is significantly more than data scientists with 50% remote work but still less than data scientists with zero remote work.")

