import csv
import numpy as np
import tensorflow as tf

time_step = [] 
sunspots = []

# Load csv file and append data to time_step list
# and sunspots list



# list to numpy array 
series = np.array(sunspots)
time = np.array(time_step)

split_time = 3000
time_train = time[:split_time]
x_train = series[:split_time]
time_valid = time[split_time:]
x_valid = series[split_time:]

window_size = 60
batch_size = 32
shuffle_buffer_size = 1000

# create windowed dataset


# train model


model = _


# predictions
forecast=[]
for time in range(len(series) - window_size):
  forecast.append(model.predict(series[time:time + window_size][np.newaxis]))

# forecast
forecast = _
results = np.array(forecast)[:, 0, 0]

# evaluation

tf.keras.metrics.mean_absolute_error(x_valid, results).numpy()


# save 
model.save('exercice5.h5')