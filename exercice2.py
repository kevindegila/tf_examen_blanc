import tensorflow as tf
import numpy as np
from tensorflow import keras

# Data
xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)

# model et training

model = _

print(model.predict([7.0]))
     

# Sauvegarde

model.save("exercice2.h5")