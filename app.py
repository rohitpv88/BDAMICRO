import numpy as np
import pickle
import streamlit as st
loading_model=pickle.load(open('diabetics_prediction.pkl','rb'))
def predict(input_data):
    in_data_array=np.asarray(input_data)
    input_data_reshape=in_data_array.reshape(1,-1)
    prediction=loading_model.predict(input_data_reshape)
    print(prediction)
    if(prediction[0]==0):
        return 'Not Affected'
    else:
        return 'Affected'
def main():
    st.title('Liver Disease Predictor')
    Age= st.text_input('Age')
    Bilirubin= st.text_input('Bilirubin')
    AlkalinePhosphotase=st.text_input('Alkaline Phosphotase')
    AlamineAminotransferase=st.text_input('Alamine Aminotransferase')
    AspartateAminotransferase=st.text_input('Aspartate Aminotransferase')
    Protiens=st.text_input('Protiens')
    Albumin=st.text_input('Albumin')
    ABR=st.text_input('Albumin and Globulin Ratio')
    diagnosis = ' '
    if st.button("Predict"):
        diagnosis = predict([Age,Bilirubin,AlkalinePhosphotase,AlamineAminotransferase,AspartateAminotransferase,Protiens,Albumin,ABR])
    st.success(diagnosis)
if __name__  == '__main__':
    main()
