#-*-coding:utf8-*-

import os
import cv2


#Read the files with certain suffix into a list. The first element is the folder name.

def readAllImg(path,*suffix):
    try:

        s = os.listdir(path)
        resultArray = []
        fileName = os.path.basename(path)
        resultArray.append(fileName)

        for i in s:
            if endwith(i, suffix):
                document = os.path.join(path, i)
                img = cv2.imread(document)
                resultArray.append(img)


    except IOError:
        print ("Error")

    else:
        print ("Ok")
        return resultArray

#Input a string and a label. Math the string with the label.

def endwith(s,*endstring):
   resultArray = map(s.endswith,endstring)
   if True in resultArray:
       return True
   else:
       return False

if __name__ == '__main__':

  result = readAllImg("D:\proj\dataset\guangchao",'.pgm')
  print (result[0])
