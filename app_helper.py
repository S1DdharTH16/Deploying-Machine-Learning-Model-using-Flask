from tensorflow.keras.preprocessing.image import load_img,img_to_array
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import PIL

def p(file_path):

 
 img = load_img(file_path,target_size=(256,256))
 img= img_to_array(img)

 img =img.reshape(-1,256,256,3)
 m=tf.keras.models.load_model('fire_cnn_model.h5')

 p=m.predict(img)

 if p[0][0]==0:
    re='fire'
 else:
    re='smoke'



 return re
 


    
   