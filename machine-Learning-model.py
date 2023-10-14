import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Load the pre-trained VGG16 model with weights trained on ImageNet
base_model = VGG16(weights='imagenet', include_top=False)

# Add a global average pooling layer and a dense layer for binary classification
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Freeze the layers of the pre-trained model (optional)
for layer in base_model.layers:
    layer.trainable = False

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Example usage for inference (after training on your dataset)
photo_path = "captured_photo.jpg"

# Load and preprocess the photo (resize, normalize, etc.)
image = tf.keras.preprocessing.image.load_img(photo_path, target_size=(224, 224))
image = tf.keras.preprocessing.image.img_to_array(image)
image = tf.keras.applications.vgg16.preprocess_input(image)
image = tf.convert_to_tensor(image)

# Perform inference on the photo to classify it
result = model.predict(tf.expand_dims(image, axis=0))

if result >= 0.5:
    print("Photo meets DV Lottery requirements.")
else:
    print("Photo does not meet requirements.")
