import numpy as np
import cv2
from keras.preprocessing import image
from keras.utils import load_img, img_to_array
from keras.applications.resnet import ResNet50, decode_predictions, preprocess_input

# Load the ResNet50 model
model = ResNet50(weights='imagenet')

# predictions 
def prediction(path):
    img_path = path
    img = load_img(img_path, target_size=(224, 224))

    # Preprocess the image
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Use the ResNet50 model to predict the image class
    preds = model.predict(x)
    pred_class = decode_predictions(preds, top=1)[0][0][1]

    return pred_class

# video path
video_path = "video.mp4"
video = cv2.VideoCapture(video_path)

while True:
    ret, frame = video.read()
    if not ret:
        break
    else:
        cv2.imwrite("temp.png",frame)
        prediction_text = prediction("temp.png")
        cv2.putText(frame, f"Prediction : {prediction_text.title()}", (525,74), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255,204,51), 4)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
video.release()# Releases video capture module
cv2.destroyAllWindows()# close all cv2 windows