import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Experience vs Salary ML Prediction")
nav = st.sidebar.radio("Navigation", ['Home', 'Prediction', 'Contribute'])

data = pd.read_csv('Salaries.csv')
x = np.array(data['yrs.service']).reshape(-1, 1)
lr = LinearRegression()
#lr.fit(x, np.array(data['salary']))

if nav == 'Home':
    st.image('Minimum-wage-and-salary.jpg')
    if st.checkbox('Show Salary Table'):
        st.table(data)
        
    graph = st.selectbox('What type of graph?', ['Non-Interactive', 'Interactive'])

    val = st.slider('Filter data using Years of service', 0,60)
    data = data.loc[data['yrs.service'] >= val]
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
    st.header("Know your Salary")
    val = st.number_input("Enter you exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred =lr.predict(val)[0]
    if st.button("Predict"):
        st.success(f"Your predicted salary is £{round(pred)}")
    
if nav == 'Contribute':
    st.image('Salery.jpg')
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your of Service", 0.0, 20.0)
    sal = st.number_input("Enter your Salary", 0.00, 1000000.00, step=1000.0)
    if st.button("submit"):
        to_add = {"yrs.service": [ex], "salary": [sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salaries.csv", mode='a',
                      header=False, index=False)
        st.success("Submitted")
