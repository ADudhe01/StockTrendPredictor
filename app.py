import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from datetime import datetime
import yfinance as yf
import streamlit as st

from tensorflow.keras.models import load_model

start = '2000-01-01'
end = datetime.today().strftime('%Y-%m-%d')

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = yf.download(user_input, start, end)

# Describing data
st.subheader('Data from 2000 - present')
st.write(df.describe())

#Visualizations
st.subheader('Closing price v/s Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.xlabel('Year')
plt.ylabel('Price')
st.pyplot(fig)


st.subheader('Closing price v/s Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close)
plt.xlabel('Year')
plt.ylabel('Price')
st.pyplot(fig)


st.subheader('Closing price v/s Time chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100, 'r', label='MA100')
plt.plot(ma200, 'g', label='MA200')
plt.plot(df.Close, label='Closing')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig)


# splitting data into training and testing on Close column
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))   

data_training_array = scaler.fit_transform(data_training)

#Load the model
model = load_model('keras_model.h5')

#Testing part
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
  x_test.append(input_data[i-100:i])
  y_test.append(input_data[i, 0])
  
x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)

scaler = scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor


#Final graph
st.subheader('Predictions v/s Original')
fig2 = plt.figure(figsize = (12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

st.pyplot(fig2)