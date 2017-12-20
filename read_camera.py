# -*- coding:utf-8 -*-

import cv2
from train_model import Model
from read_data import read_name_list

class Camera_reader(object):

    #Load model
    def __init__(self):
        self.model = Model()
        self.model.load()
        self.img_size = 128


    def build_camera(self):        
        face_cascade = cv2.CascadeClassifier('D:\proj\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_alt.xml')
        #Read the subfolder in dataset folder
        name_list = read_name_list('D:\proj\dataset')

        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()

        while success and cv2.waitKey(1) == -1:
             success, frame = cameraCapture.read()
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             faces = face_cascade.detectMultiScale(gray, 1.3, 5)
             for (x, y, w, h) in faces:
                 ROI = gray[x:x + w, y:y + h]
                 ROI = cv2.resize(ROI, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                 label,prob = self.model.predict(ROI)
                 if prob >0.7:    #Only output higher than 70% label
                     show_name = name_list[label]
                 else:
                     show_name = 'Stranger'
                 cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
                 frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
             cv2.imshow("Camera", frame)

        cameraCapture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = Camera_reader()
    camera.build_camera()


