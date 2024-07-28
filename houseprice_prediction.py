import streamlit as st
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import pickle

model = pickle.load(open("predict_pl.pkl","rb"))

st.image(r"House.jpg")

st.title("House-Price Prediction Project")


SquareFeet = st.number_input("Enter the SquareFeet:",key='input1')
Bedrooms = st.number_input("Select the number of bed rooms:",min_value = 1,max_value = 4, key='input2')
Bathrooms= st.number_input("Select the number of bed rooms:",min_value = 1,max_value = 4, key='input3')
Neighborhood= st.selectbox("Select the Neighborhood:",["Rural","Suburb","Urban"])
YearBuilt= st.number_input("Select the Year Built:")

 
if st.button("Submit"):
    prediction = model.predict([[SquareFeet,Bedrooms,Bathrooms,Neighborhood,YearBuilt]])[0]
    st.write("The predicted value is:", prediction)

