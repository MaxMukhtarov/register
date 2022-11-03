import numpy as np
import os
import cv2
import face_recognition
import json
from datetime import date
from tkinter import messagebox
import datetime

path = 'oquvchilar'
images = []
classNames = []
myList = os.listdir(path)


for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
dict = {}
n=0
for i in images:
    img = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    dict[classNames[n]] = list(encode)
    n+=1

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
        data.update(dict)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=3)
except:
    with open('data.json', 'w') as file:
            json.dump(dict, file, indent=3)
