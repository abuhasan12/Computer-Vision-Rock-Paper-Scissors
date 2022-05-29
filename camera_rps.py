import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    start = time.time()
    while time.time() < start + 5:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        if prediction[0][0] > 0.5:
            users_rps = "Rock"
        elif prediction[0][1] > 0.5:
            users_rps = "Paper"
        elif prediction[0][2] > 0.5:
            users_rps = "Scissors"
        else:
            users_rps = "Nothing"
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return users_rps

user_choice = get_prediction()
print(user_choice)
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()