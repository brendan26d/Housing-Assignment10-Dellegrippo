import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing: Brendan Dellegrippo')
df = pd.read_csv('housing.csv')

cost_filter = st.slider('Median Housing Price:', 200000, 500001, 0)  # min, max, default

location_filter = st.sidebar.multiselect(
     'Location Selector:',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  

df = df[df.median_house_value >= cost_filter]
df = df[df.ocean_proximity.isin(location_filter)]

income_filter = st.sidebar.radio(
     "Choose income level:",
     ('Low', 'Medium', 'High'))
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

income = income_filter
form = st.form("income_filter")


# show on map
st.map(df)


# restrain x axis by min and max values of slider
# y axis is number of houses in said range
st.title('Histogram of Median House Value')
fig, ax = plt.subplots()
df.median_house_value.plot.hist(ax=ax, bins = 30)
st.pyplot(fig)
