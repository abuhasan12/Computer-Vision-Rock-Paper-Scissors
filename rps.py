import random
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

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_winner(computer_choice, user_choice):
    pairs = [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")]
    if (computer_choice, user_choice) in pairs:
        return "Computer"
    elif (user_choice, computer_choice) in pairs:
        return "User"
    else:
        return "Draw"

def play_with_camera():
    computer_wins = 0
    user_wins = 0
    while computer_wins < 3 and user_wins < 3:
        input("Get ready for the round! (press enter)")
        user_choice = get_prediction()
        computer_choice = get_computer_choice()

        print(f"\nComputer picks: {computer_choice}")
        print(f"User picks: {user_choice}")

        winner = get_winner(computer_choice, user_choice)
        if winner == "Draw":
            print("It's a Draw.")
        else:
            if winner == "Computer":
                computer_wins += 1
            else:
                user_wins += 1
            print(f"{winner} wins.")
    print(f"{winner} won three rounds first!")

play_with_camera()