#-*-coding:utf8-*-

from read_data import read_name_list,read_file
from train_model import Model
import cv2

def test_onePicture(path):
    model= Model()
    model.load()
    img = cv2.imread(path)
    img = cv2.resize(img, (64, 64))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    picType,prob = model.predict(img)
    if picType != -1:
        name_list = read_name_list('D:\myProject\pictures\dataset')
        print (name_list[picType],prob)
    else:
        print (" Don't know this person")

#Read images in the folder and subfolders

def test_onBatch(path):
    model= Model()
    model.load()
    index = 0
    img_list, label_lsit, counter = read_file(path)
    for img in img_list:
        picType,prob = model.predict(img)
        if picType != -1:
            index += 1
            name_list = read_name_list('D:\proj\dataset')
            print (name_list[picType])
        else:
            print (" Don't know this person")

    return index

if __name__ == '__main__':
    test_onePicture('D:\proj\dataset\pic.jpg')



