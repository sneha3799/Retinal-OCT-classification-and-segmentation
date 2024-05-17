from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array
import pickle
import cv2
import numpy as np

#from keras.models import load_model
#model = load_model('my_model.h5')
names = ["Normal", "CNV", "DME", "Drusen"]

def processImg(IMG_PATH):
    # Read image
    model = pickle.load(open('classification.pkl','rb'))

    # Preprocess image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (224, 224))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    print(image.shape)
    image = np.expand_dims(image, axis=0)

    res = model.predict(image)
    label = np.argmax(res)
    print("Label", label)
    labelName = names[label]
    print("Label name:", labelName)
    return labelName

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/classify',methods=['POST'])
def processReq():
    data = request.files["scan"]
    data.save("img.jpg")
    resp = processImg("img.jpg")
    return render_template('index.html',result=resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

