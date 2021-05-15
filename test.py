import os
import sys
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from keras.models import load_model
import tensorflow as tf
graph = tf.get_default_graph()

def loading_model():
    model=load_model('ml.h5')
    print('model loaded')
    return model

def predcit(url,model):
    response=requests.get(url)
    img=Image.open(BytesIO(response.content))
    img=np.array(img.resize((28,28)))
    a=img.reshape(-1,28,28,1)
    print(a)
    with graph.as_default():
        b=model.predict(a)
    label=np.argmax(b)
    print(label)
    return(label)


    
