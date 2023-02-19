from config import DefaultSetup
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import InputLayer, MaxPool2D
from tensorflow.python.keras.layers import Conv2D, MaxPool2D, Flatten
from tensorflow.python.keras.losses import categorical_crossentropy
from tensorflow.python.keras.optimizers import rmsprop_v2


conv2d_filters = DefaultSetup.TRAIN.CONV2D_FILTERS

m1 = Sequential([
    InputLayer(input_shape=(150, 150, 4), batch_size=32),
    Conv2D(filters=conv2d_filters[0], kernel_size=7, activation='leaky_relu'),
    MaxPool2D(pool_size=2),
    Conv2D(filters=conv2d_filters[1], kernel_size=3, activation='leaky_relu'),
    MaxPool2D(pool_size=2),
    Conv2D(filters=conv2d_filters[2], kernel_size=3, activation='leaky_relu'),
    MaxPool2D(pool_size=2),
    Conv2D(filters=conv2d_filters[3], kernel_size=3, activation='leaky_relu'),
    MaxPool2D(pool_size=2),
    Conv2D(filters=conv2d_filters[4], kernel_size=3, activation='leaky_relu'),
    MaxPool2D(pool_size=2),
    Flatten()
])

m1.compile(
        loss=categorical_crossentropy,
        optimizer=rmsprop_v2.RMSProp(learning_rate=1e-5, momentum=0.90)
)

m1.summary()
