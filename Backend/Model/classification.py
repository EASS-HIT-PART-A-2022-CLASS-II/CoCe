import numpy as np

from keras.models import load_model
from keras.utils import load_img, img_to_array

model = load_model(filepath = "Model/final_model.h5")

# The value will be displayed to the user according to the classification of the neural network.
results = {0:"Airplane", 1:"Automobile", 2:"Bird", 3:"Cat", 4:"Deer", 5:"Dog", 6:"Frog", 7:"Horse", 8:"Ship", 9:"Truck"}

def classification_process(filepath):
    # Will load the input image and force it to the size of 32x32 pixels.
    image = load_img(path = filepath, target_size = (32, 32))
    
    # Machines see an input image as an array of pixels, so we have to convert our input image into an array of pixels.
    image = img_to_array(img = image)
    
    # Will reshape the array (We’ve now working with a numpy array and not the input image itself) into a single sample with 
    # 3 dimensions (or channels).
    image = image.reshape(1, 32, 32, 3)
    
    # The pixel values of the input image must be normalized as the pixel values we’ve trained the neural network upon.
    image = image.astype(dtype = "float32")
    image = image / 255.0
    
    # "np.argmax()" will return the index of the highest probability score in the probability array produced by the neural 
    # network.
    result = results[np.argmax(a = model.predict(image))]

    return result