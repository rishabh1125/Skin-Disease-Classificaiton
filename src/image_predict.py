import tensorflow as tf
import numpy as np
import os
from pathlib import Path
import sys
sys.path.append(Path(os.path.abspath(__file__)).parent.parent) 
class ImageClassification:
    labels = ['Eczema','Acne','Milia','Rosacea','Keratosis','Carcinoma']    
    def classify_image(self, image: str, model:str):
        # Placeholder for image classification logic
        prediction = None
        image = tf.io.read_file(image)
        image = tf.image.decode_jpeg(image, channels=3)
        print(image.shape)
        image = tf.image.resize(image, [224, 224])
        image = tf.expand_dims(image, 0)
        if model == "CNN trained":
            model = tf.keras.models.load_model("models/cnn_model.h5")
            prediction = model.predict([image])
            prediction = dict(zip(self.labels,prediction[0]))
            prediction = sorted(prediction.items(), key=lambda x:x[1], reverse=True)
            prediction = list(map(lambda x: (x[0], round(x[1] * 100, 2)), prediction))
            return prediction
        elif model == "Finetuned ResNet50":
            model = tf.keras.models.load_model("models/resnet_50_finetuned.h5")
            prediction = model.predict([image])
            prediction = dict(zip(self.labels,prediction[0]))
            prediction = sorted(prediction.items(), key=lambda x:x[1], reverse=True)
            prediction = list(map(lambda x: (x[0], round(x[1] * 100, 2)), prediction))
            print(prediction)
            return prediction
        else:
            raise ValueError("Invalid model")
        