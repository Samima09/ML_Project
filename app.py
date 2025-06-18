import streamlit as st
import pandas as pd
import numpy as np
from src.components.custom_data import CustomData
from src.pipeline.predict_pipeline import PredictPipeline

st.set_page_config(page_title="Student Exam Performance Predictor")

st.title("🎓 Student Exam Performance Prediction")

# Form inputs
gender = st.selectbox("Select Gender", ['male', 'female'])
ethnicity = st.selectbox("Select Ethnicity", [
    'group A', 'group B', 'group C', 'group D', 'group E'])
parental_level_of_education = st.selectbox("Parental Level of Education", [
    "associate's degree", "bachelor's degree", "master's degree", 
    "some college", "high school", "some high school"])
lunch = st.selectbox("Lunch Type", ['standard', 'free/reduced'])
test_preparation_course = st.selectbox("Test Preparation Course", ['none', 'completed'])
reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100)
writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100)

# Predict button
if st.button("Predict Total Score"):
    # Create data object
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )
    df = data.get_data_as_dataframe()

    # Make prediction
    pipeline = PredictPipeline()
    result = pipeline.predict(df)

    st.success(f"🎯 Predicted Math Score: **{result[0]:.2f}**")
