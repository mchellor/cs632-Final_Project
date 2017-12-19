# cs632-Final_Project

Student ID:U01366690

Name: Guangchao Chen

This is the final project for class CS632L.
Project detail: In my project, I build a program that can be train to recognize people via their face. The idea is that this program uses a model which is trained by photos. Then, program calls webcam and find and mark the face in video.

Main program instruction:
1. pick_face.py    Detect faces in photo. Reform and restore the face image.
2. train_model.py    Train the model.
3. read_camera.py    Load the model and call webcam to detect people.

Processing:
Step 1: Preparing training data. In order to collect training data, I use the Haar Feature-based Cascade Classifiers which is default in Opencv to detect face in photo. Then the program will reform and restore the face images. To label these face images, put them in different folder and program will use the folder name as its label. In my case, I collect a bunch of photos that contain people face. Here I use my photo and my wife's photo to train my model.

Step 2: Build model and train data. In my program, I build a CNN model (still improving its performance) which is quite a similiar idea as our assignment 2. 

Step 3: Call webcam and verify our accurancy. Program will call the webcam and show a frame with the name of training.


Still need improvement. 1. Need more data for training. 2. Modify model to enhance accurancy.

Video: Still working...
