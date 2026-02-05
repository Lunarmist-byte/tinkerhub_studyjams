import tensorflow as tf
import numpy as np
print("Loading Fasion Data")
(train_images,train_labels),(test_images,test_labels)=tf.keras.datasets.fashion_mnist.load_data()
train_images=train_images/255.0
test_images=test_images/255.0
class_names=['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
model=tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation='relu'),tf.keras.layers.Dense(10,activation='softmax')])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
print("Training the brain on 60k images")
model.fit(train_images,train_labels,epochs=5)
print("\n--TEST PREDICTION---")
test_img=test_images[100]
prediction=model.predict(np.array([test_img]))
predicted_index=np.argmax(prediction)
print(f"AI Predicts:{class_names[predicted_index]}")
print(f"Actual Label:{class_names[test_labels[100]]}")
