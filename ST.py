import streamlit as st
import joblib
import numpy as np


model = joblib.load("STUDENT_PERFORMANCE.pkl")
scaler = joblib.load("SCALER.pkl")



st.title("👩‍🎓 Welcome to Student Performance Check Application")

study_hour = st.selectbox('📚 Enter a numbers of hour you studied: ',[0,1,2,3,4,5,6,7,8,9,10])
previous_score = st.number_input('💯 Enter your previous score: ',min_value=0,max_value=100)
sleep_hour = st.number_input('😴 Enter the number of hours you sleep:',min_value=0,max_value=24)
sampel_paper =st.number_input('📜Number of sample papers you solved: ',min_value=0,max_value=50)
activity_inlovement=st.radio('🏐 Are you involved in extra curricular activities?',['Yes','No'])

filter = 1 if activity_inlovement =='Yes' else 0

if st.button('🎯 Predict the Performence'):
    input =[[study_hour,previous_score,sleep_hour,sampel_paper,filter]]
    scaling = scaler.transform(input)
    predict = model.predict(scaling)
    percent = round(predict[0],2)
    st.success(f'Your Performence is {percent}%')


            
            