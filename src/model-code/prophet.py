import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from prophet import Prophet
import pickle
from google.colab import files

uploaded = files.upload()

df = pd.read_csv('CPI_data.csv')

# Convert date column data into a date object
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

# Extract columns in the dataset
df.columns = ['ds', 'y']
df.head()

# split data into training and test sets
train_set = df.iloc[:456]
test_set = df.iloc[456:]

# Training the model
m = Prophet(interval_width=0.90)
model = m.fit(train_set)

future = m.make_future_dataframe(periods=36, freq='MS')
forecast = m.predict(future)

# Viewing the forecast data
forecast[['ds','yhat']]

# save the trained model to a file
with open('trained_prophet_model.pkl', 'wb') as f:
    pickle.dump(model, f)

files.download('trained_prophet_model.pkl')