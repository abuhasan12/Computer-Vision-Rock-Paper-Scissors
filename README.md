# Computer-Vision-Rock-Paper-Scissors

The Computer Vision Rock Paper Scissors project is to simulate a rock-paper-scissors game with your computer. It uses a TensorFlow model to identify if you are holding up 'rock', 'paper', 'scissors' or 'nothing' to your camera.

## Milestone 1 - Creating the Model

The model was created using Teachable Machine with Google. It is a standard image-based model using four classes - Rock, Paper, Scissors and Nothing. The images for the classes to train the model were captured by the developer and then exported as a TensorFlow Keras model.

## Milestone 2 - Create Virtual Environment, Install Dependencies and Run Model

A new conda environment was created with the opencv-python, tensorflow and ipykernel libraries installed via pip. The code in modelcode.py was used in model.ipynb to run the model. Running the file will pop up a camera to detect if you are holding up rock, paper or scissors. The code includes if-elif-else statements to print what you are holding up.

## Milestone 3 - Create a Rock-Paper-Scissors game

manual_rps.py includes a scripting rock-paper-scissors game. It consists of the functions get_computer_choice, which randomly generates one of the optons, and get_user_choice, which asks for the user's input for one of the options. The get_winner function takes both choices and determines the winner using if-elif-else statements. The file uses the play function to run the game.

## Milestone 4 - Use the Camera to play Rock-Paper-Scissors

using the code in model.ipynb, a new file called camera_rps.py was created which contains the code and a function, get_prediction, for the camera input of rock-paper-scissors. rps.py is the file that contains the rock-paper-scissors game with the computer using a camera. It uses the get_prediction function, as well as get_computer_choice for the user and computer inputs. The get_winner function determines a winner and play_with_camera function allows for multiple rounds until either the user or computer has won 3 times.
