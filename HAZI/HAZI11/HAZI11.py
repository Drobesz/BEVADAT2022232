# %%

import tensorflow as tf
import numpy as np

'''
Készíts egy metódust ami a cifar100 adatbázisból betölti a train és test adatokat. (tf.keras.datasets.cifar100.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: cifar100_data
'''



# %%
def cifar100_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar100.load_data()
    train_images = train_images.astype('float32') / 255.0
    test_images = test_images.astype('float32') / 255.0
    
    return train_images, train_labels, test_images, test_labels
    

# %%
train_images, train_labels, test_images, test_labels = cifar100_data()

# %%
'''
Készíts egy konvolúciós neurális hálót, ami képes felismerni a képen mi van a 100 osztály közül.
A háló kimenete legyen 100 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet..


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: cifar100_model
'''


# %%
def cifar100_model() -> tf.keras.Sequential:
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(filters = 64,
                               kernel_size = (3, 3),
                               strides = (1, 1),
                               activation = tf.keras.activations.relu,
                               input_shape = (32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(filters = 64,
                               kernel_size = (3, 3),
                               strides = (1, 1),
                               activation = tf.keras.activations.relu,
                               input_shape = (32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Conv2D(filters = 64,
                               kernel_size = (3, 3),
                               strides = (1, 1),
                               activation = tf.keras.activations.relu,
                               input_shape = (32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation = 'relu'),
        tf.keras.layers.Dense(100, activation = 'softmax')
    ])
    return model

# %%
model = cifar100_model()

# %%
'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''


# %%
def model_compile(model) -> tf.keras.Sequential:
    model.compile(optimizer = 'adam', 
                  loss = tf.losses.SparseCategoricalCrossentropy(from_logits = False),
                  metrics = ['accuracy'])
    return model

# %%
model_compile(model)

# %%
'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labelsz
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''


# %%
def model_fit(model, epochs, train_images, train_labels) -> tf.keras.Sequential:
    model.fit(train_images, train_labels, epochs = epochs, batch_size = 128, verbose = 2)
    return model

# %%
#model_fit(model, 16, train_images, train_labels)

# %%
'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''


# %%
def model_evaluate(model, test_images, test_labels) -> tuple[np.ndarray, np.ndarray]:
    model.evaluate(test_images, test_labels, batch_size = 128)
    return

# %%
model_evaluate(model, test_images, test_labels)


