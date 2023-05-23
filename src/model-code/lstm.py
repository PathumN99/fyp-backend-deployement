import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense
import pickle

# Uploading the dataset file
uploaded = files.upload()

# Load the data
df = pd.read_csv('CPI_data.csv', index_col='date', parse_dates=True)

# split data into training and test sets
train_set = df.iloc[:456]
test_set = df.iloc[456:]

results = seasonal_decompose(df['CPI'])
results.plot()

# Normalize the data
scaler = MinMaxScaler()
scaler.fit(train_set)

scaled_train = scaler.transform(train_set)
scaled_test = scaler.transform(test_set)

# Define generator
n_input = 12
n_features = 1
generator = TimeseriesGenerator(scaled_train, scaled_train, length = n_input, batch_size = 1)

# Create the LSTM model
model = Sequential()
model.add(LSTM(100, activation = 'relu', input_shape=(n_input, n_features)))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# fit the model
model.fit(generator, epochs = 50)

last_train_batch = scaled_train[-12:]

last_train_batch = last_train_batch.reshape((1, n_input, n_features))

model.predict(last_train_batch)

test_predictions = []

first_eval_batch = scaled_train[-n_input:]
current_batch = first_eval_batch.reshape((1, n_input, n_features))

for i in range(len(test_set)):
  # get the prediction value for the first batch
  current_pred = model.predict(current_batch)[0]

  # append the prediction into the array
  test_predictions.append(current_pred)

  # use the predcition to update the batch and remove the first value
  current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

# Viewing the untransformed prediction
test_predictions

# transforming into a readable prediction
true_predictions = scaler.inverse_transform(test_predictions)

# Viewing the final prediction
true_predcitions

# save the trained model as a pkl file
with open('trained_lstm_model.pkl', 'wb') as f:
    pickle.dump(model, f)

files.download('trained_lstm_model.pkl')
