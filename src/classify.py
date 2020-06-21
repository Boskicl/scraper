import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import decode_predictions
import requests
import glob

class classify:
    def __init__(self,folder):
        self.folder     = folder
        self.path       = '/home/local/DEVNET/boskicl/scripts/data_scrapper/data/data_' + self.folder + '/img/*.jpg'
    def process(self):
        model = tf.keras.applications.Xception(
            include_top=True,
            weights="imagenet",
            input_tensor=None,
            input_shape=None,
            pooling=None,
            classes=1000,
            )
        image_list = []
        # Go through data folder and find all .jpeg(s) and put into a list
        for filename in glob.glob(self.path):
            image_list.append(filename)
        # From list of images, go through all and do classification for each
        for images in image_list:
            img=tf.keras.preprocessing.image.load_img(images,target_size=(299,299))
            img=tf.keras.preprocessing.image.img_to_array(img)

            response=requests.get('https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json')
            imgnet_map=response.json()

            img=tf.keras.applications.xception.preprocess_input(img)
            predictions = model.predict(np.array([img]))
            # Make predictions (top 3) - Only care about top on decode[0][0][1], second decode[0][1][1]
            decode = decode_predictions(predictions,top=3)

            start = "\033[1m" # For Bold setting (before)
            end = "\033[0;0m" # For Bold setting (after)
            print('Prediction of : ' + start + '{0}'.format(decode[0][0][1]) + end + ' for image : ' + start + '{0}'.format(images.strip(self.path)) + end + ' with confidence : ' + start + '{0}'.format(decode[0][0][2]) + end)

# ## Testing uncomment for only that part
classes = classify('tree')
classes.process()
