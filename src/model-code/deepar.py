import pandas as pd
from gluonts.dataset.common import ListDataset
from gluonts.mx.model.deepar import DeepAREstimator
from gluonts.mx.trainer import Trainer
from gluonts.evaluation.backtest import make_evaluation_predictions
from gluonts.evaluation import Evaluator
import matplotlib.pyplot as plt
import pickle
from google.colab import files

# Uploading the dataset file
uploaded = files.upload()

# read in the time series data
data = pd.read_csv("CPI_data.csv", index_col="date", parse_dates=True)

# split data into training and validation sets
train_data = data.iloc[:456]
val_data = data.iloc[456:]

# create a GluonTS ListDataset object for training data
training_data = ListDataset(
    [{"start": train_data.index[0], "target": train_data["CPI"].values}],
    freq="M"
)

# define the DeepAR estimator object
estimator = DeepAREstimator(
    freq="M",
    prediction_length=24,
    context_length=12,
    num_layers=2,
    num_cells=40,
    trainer=Trainer(epochs=50)
)

# train the model on the training data
predictor = estimator.train(training_data=training_data)

# create a GluonTS ListDataset object for validation data
validation_data = ListDataset(
    [{"start": val_data.index[0], "target": val_data["CPI"].values}],
    freq="M"
)

# make predictions on the validation data
forecast_it, ts_it = make_evaluation_predictions(
    dataset=validation_data, predictor=predictor, num_samples=100
)

forecast = next(forecast_it)

# extract the predicted values from the forecast
forecast_values = forecast.mean.tolist()

forecast_values

# save the trained model as a pkl file
with open('trained_deepar_model.pkl', 'wb') as f:
    pickle.dump(predictor, f)

files.download('trained_deepar_model.pkl')