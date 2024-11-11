import numpy as np
import pickle
import streamlit as st

loading_model = pickle.load(open('diabetics_prediction.pkl','rb'))


def dia_prediction(input_data):
    in_data_array = np.asarray(input_data)

    input_data_reshape = in_data_array.reshape(1, -1)

    prediction = loading_model.predict(input_data_reshape)
    print(prediction)

    if(prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    



def main():
    st.title('Diabetics Predictor')

    Pregnancies = st.text_input('Enter the Pregnancies')
    Glucose = st.text_input('Enter the Glucode Level')
    BloodPressure = st.text_input('Enter the BloodPressure')
    SkinThickness = st.text_input('Enter the SkinThickness')
    Insulin = st.text_input('Enter the Insulin Level')
    BMI = st.text_input('Enter the BMI')
    DiabetesPedigreeFunction = st.text_input('Enter the DiabetesPedigreeFunction')
    Age = st.text_input('Enter the Age')

    diagnosis = ' '

    if st.button("Check Diabetes"):
        diagnosis = dia_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)



if __name__  == '__main__':
    main()