import numpy as np
import pickle

loading_model = pickle.load(open('diabetics_prediction.pkl','rb'))

input_data = (5,166,72,19,175,25.8,0.587,51)

in_data_array = np.asarray(input_data)

input_data_reshape = in_data_array.reshape(1, -1)

prediction = loading_model.predict(input_data_reshape)
print(prediction)

if(prediction[0] == 0):
    print('The person is not diabetic')
else:
    print('The person is diabetic')