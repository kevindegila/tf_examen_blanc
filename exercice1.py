import tensorflow as tf
import numpy as np
from tensorflow import keras

# Data
xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Définis et compile ton modèle
model = _


# Prédiction
print(model.predict([10.0]))


# Sauvegarde
model.save("exercice1.h5")