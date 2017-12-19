#-*-coding:utf8-*-

import os
import cv2
import time
from read_img import readAllImg

#Read all the images in the sourcepath and put into a list. Then check one by one, cut the face out and save in objectpath
def readPicSaveFace(sourcePath,objectPath,*suffix):
    try:
        #Read image
        resultArray=readAllImg(sourcePath,*suffix)

        #Check the image in the list one by one. Find the face and put into the object path
        
        count = 1
        face_cascade = cv2.CascadeClassifier('D:\proj\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_alt.xml')
        for i in resultArray:
            if type(i) != str:

              gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
              faces = face_cascade.detectMultiScale(gray, 1.3, 5)
              for (x, y, w, h) in faces:
                listStr = [str(int(time.time())), str(count)]
                fileName = ''.join(listStr)

                f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                cv2.imwrite(objectPath+os.sep+'%s.jpg' % fileName, f)
                count += 1


    except IOError:
        print ("Error")

    else:
        print ('Already read '+str(count-1)+' Faces to Destination '+objectPath)

if __name__ == '__main__':
     readPicSaveFace('D:\proj\pickdata','D:\proj\data','.jpg','.JPG','png','PNG')



