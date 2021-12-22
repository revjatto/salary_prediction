import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px

st.title("Salary Prediction application")
nav = st.sidebar.radio("Navigation", ['Home', 'Prediction', 'Contribute'])

data = pd.read_csv('Salaries.csv')

if nav == 'Home':
    st.image('Minimum-wage-and-salary.jpg')
    if st.checkbox('Show Salary Table'):
        st.table(data)
        
graph = st.selectbox('What type of graph?', ['Non-Interactive', 'Interactive'])

val = st.slider('Filter data using Years of service', 0,60)
if graph == 'Non-Interactive':
    fig = plt.figure(figsize=(10,5))
    plt.scatter(data['yrs.service'],data['salary'])
    plt.ylim(0)
    plt.xlabel('Years of Service')
    plt.ylabel('Yearly Salary')
    plt.tight_layout()
    st.pyplot(fig)
    
if graph == "Interactive":
    layout = go.Layout(
        xaxis=dict(range=[0, 16]),
        yaxis=dict(range=[0, 210000])
    )
    fig = go.Figure(data=go.Scatter(
        x=data["yrs.service"], y=data["salary"], mode='markers'), layout=layout)
    st.plotly_chart(fig)

if nav == 'Prediction':
    st.image('salary_people.jpg')
    
if nav == 'Contribute':
    st.image('Salery.jpg')
