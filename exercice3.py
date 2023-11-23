import tensorflow as tf

# Dataset
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Preprocessing

# Model training
model = _

# Evaluation

test_loss = model.evaluate(test_images, test_labels)
print(test_loss)

# Sauvegarde
model.save("exercice3.h5")