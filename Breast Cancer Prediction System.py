# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:21:37 2023

@author: Scofield
"""

import numpy as np
import pickle
import streamlit as st

# Loading the production model
production_model = pickle.load(open('C:/Users/Scofield/Breast_cancer_predictive_model.sav', 'rb')) # rb means read binary

# Creating a function 
def perform_breat_cancer_test(input_data):
    
    # Converting the input data into an array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # Reshaping the array because we are predicting only one instance
    reshaped_input_data = input_data_as_numpy_array.reshape(1, -1)
    
    prediction = production_model.predict(reshaped_input_data)
    
    if prediction[0]==0:
        
        return 'This patient is healthy'
    
    else:
        
        return 'This patient has breast cancer'


# Creating the main function

def main():
    
    # Give the app a captivating tittle
    st.title("BREAST CANCER PREDICTIVE SYSTEM")
    
    
    # Create input text boxes

    
    mean_radius = st.text_input("Mean radius")
    mean_perimeter = st.text_input("Mean Primeter")
    mean_area = st.text_input("Mean Area")
    mean_compactness = st.text_input("Mean Compactness")
    mean_concavity = st.text_input("Mean Concavity")
    mean_concave_points = st.text_input("Mean Concave Points")
    radius_error = st.text_input("Radius Error")
    perimeter_error = st.text_input("Primeter Error")
    area_error = st.text_input("Area Error")
    worst_radius = st.text_input("Worst Radius")
    worst_texture = st.text_input("Worst Texture")
    worst_perimeter = st.text_input("Worst Primeter")
    worst_area = st.text_input("Worst Area")
    worst_compactness = st.text_input("Worst Compactness")
    worst_concavity = st.text_input("Worst Concavity")
    worst_concave_points = st.text_input("Worst Concavity Points")
   
    
   # Code for prediction
    diagnosis = " "
   
   
    # Button for diagnosis
    if st.button("TEST FOR BREAST CANCER"):
       diagnosis = perform_breat_cancer_test([mean_radius,mean_perimeter,mean_area,mean_compactness,mean_concavity,mean_concave_points,radius_error,perimeter_error,
           area_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_compactness,worst_concavity,worst_concave_points])
    st.success(diagnosis)   
    
    
    
    
    
    
    
    
if __name__=='__main__':
    main()
       

