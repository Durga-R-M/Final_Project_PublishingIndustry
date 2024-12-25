import streamlit as st 
import pandas as pd 
import numpy as np 
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
import os

# Sidebar navigation
r = st.sidebar.radio('Main Menu', ['Home', 'Customer Churn Prediction'])

# Home Page
if r == 'Home':
    st.title('BOOKSTORE - CUSTOMER CHURN PREDICTION 📚')
    st.subheader("Data processed from the publishing industry using ANN Deep Learning")
    st.markdown("*You can predict customer churn on the next page* 😎")
    st.image("C:/Users/hp/Desktop/Final_Project/BookStore.png")  

# Customer Churn Prediction Page
elif r == 'Customer Churn Prediction':
    st.image("C:/Users/hp/Desktop/Final_Project/BookCover.png")  
    
    left_column, right_column = st.columns(2)
    p1 = left_column.slider("How many days has the customer been buying books?", 0, 1200)
    p2 = right_column.slider("How many days has the customer not returned to the shop?", 0, 1200)
    
    days = [str(day) for day in range(1, 32)]
    p3 = left_column.selectbox("Select the day the customer ordered?", days)
    
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December')
    s4 = right_column.selectbox("Select the month the customer ordered?", months)
    p4 = months.index(s4) + 1
    
    years = [str(year) for year in range(1970, 2025)]
    p5 = left_column.selectbox("Select the year the customer ordered?", years)
    p6 = right_column.slider("Price of the book bought?", 0, 500)
    p7 = left_column.number_input("How many times has the customer ordered from your shop?", min_value=0, max_value=500, value=10)
    
    # Load the model
    model = load_model('C:/Users/hp/Desktop/Final_Project/model.h5')  
    
    # Prepare input data
    input_data = np.array([[float(p6), float(p2), float(p1), float(p7), int(p3), int(p4), int(p5)]])
    
    if st.button('Predict'):
        pred = model.predict(input_data)
        predicted_class = np.argmax(pred, axis=1)[0]
        if predicted_class == 0:       
            st.success("The customer has not left the store")
        else:       
            st.success("The customer has left the store. Try to give a discount of 5%")