from tkinter import *
import os
import cv2
import face_recognition
from tkinter import filedialog

from tkinter import messagebox



root = Tk()
root.minsize(500, 500)
#======Rasm======
can = Canvas(root, width=300, height=300, bg="red")

#=====Danniy======
ism_lab = Label(root, text="Ism", width=6)
fam_lab = Label(root, text="Familiya", width=6)
grup_lab = Label(root, text="Gruppa", width=6)
ism_ent = Entry(root, width=45)
fam_ent = Entry(root, width=45)
grup_ent = Entry(root, width=45)
#=====Knopka======
btn_browse = Button(root, text="Rasm tanlash", bg="cyan", fg="white", width=20)
btn_add = Button(root, text = "Qo`shish", bg="lime", fg="black",width=20)
#======Joylash======
can.grid(row=1, column=2)
ism_lab.grid(row=2, column=1)
ism_ent.grid(row=2, column=2, columnspan=2, ipadx=82)
fam_lab.grid(row=3, column=1)
fam_ent.grid(row=3, column=2, columnspan=2)
grup_lab.grid(row=4, column=1)
grup_ent.grid(row=4, column=2, columnspan=2)
btn_browse.grid(row=5, column=1, padx=10)
btn_add.grid(row=5, column=3)
root.mainloop()
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
#
#
#
# def findEncodings(rasmlar):
#     encodeList = []
#     for img in rasmlar:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList
#
# def markAttendance(name):
#     try:
#         folderName = str(date.today()).split('-')
#         folderName = f'{folderName[0]}-{folderName[1]}'
#         os.chdir(r'C:\Users\Sehrli orolcha\Desktop\gister\kelgan')
#         os.mkdir(folderName)
#
#     except:
#          ms = messagebox.askyesno(title="So`rov", message=f"{name}\nTo`g`rimi?")
#          if ms:
#             try:
#
#                 with open(f'{folderName}/{date.today()}_bolalar.csv', 'r+') as f:
#                     myDataList = f.readlines()
#                     nameList = []
#
#                     for line in myDataList:
#                         entry = line.split(',')
#                         nameList.append(entry[1])
#
#                     if name not in nameList:
#                         now = datetime.now()
#                         datestring = now.strftime('%H:%M:%S')
#                         f.writelines(f'{len(myDataList)+1},{name},{datestring}\n')
#                         engine.say("accepted")
#
#             except FileNotFoundError:
#                 with open(f'{folderName}/{date.today()}_bolalar.csv', "w") as f:
#
#
#                     now = datetime.now()
#                     datestring = now.strftime('%H:%M:%S')
#                     f.writelines(f'1,{name},{datestring}\n')
#                     engine.say("accepted")
#                     engine.runAndWait()
#          else:
#             print("KIm bu")
# def markAttendance1(name1):
#     try:
#         folderName = str(date.today()).split('-')
#         folderName = f'{folderName[0]}-{folderName[1]}'
#         os.chdir(r'C:\Users\Sehrli orolcha\Desktop\gister\kelgan')
#         os.mkdir(folderName)
#     except:
#          ms = messagebox.askyesno(title="So`rov", message=f"{name1}\nTo`g`rimi?")
#          if ms:
#             try:
#                 with open(f'{folderName}/{date.today()}_bolalar.csv', 'r+') as f:
#                     myDataList = f.readlines()
#                     nameList = []
#
#                     for line in myDataList:
#                         entry = line.split(',')
#                         nameList.append(entry[1])
#                     if name1 not in nameList:
#                         now = datetime.now()
#                         datestring = now.strftime('%H:%M:%S')
#                         f.writelines(f'{len(myDataList)+1},{name1},{datestring}\n')
#                         engine.say('accepted')
#                         engine.runAndWait()
#             except FileNotFoundError:
#
#                 with open(f'{folderName}/{date.today()}_bolalar.csv', "w") as f:
#
#
#                     now = datetime.now()
#                     datestring = now.strftime('%H:%M:%S')
#                     f.writelines(f'1,{name1},{datestring}\n')
#                     engine.say("accepted")
#                     engine.runAndWait()
#          else:
#              print("Kim bu")
# encodeListKnown = findEncodings(images)
# print('Encoding initialized')
# cap = cv2.VideoCapture(0)
# cap1 = cv2.VideoCapture(1)
#
# while True:
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#
#     facesCurFrm = face_recognition.face_locations(imgS)
#     encodesCurFrm = face_recognition.face_encodings(imgS, facesCurFrm)
#
#     for encodeFace, faceLoc in zip(encodesCurFrm, facesCurFrm):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#
#         matchIndex = np.argmin(faceDis)
#
#
#         if matches[matchIndex] and min(faceDis)<=0.35:
#             name = (classNames[matchIndex]).upper()
#             markAttendance(name)
#             y1, x2, y2, x1 = faceLoc
#             y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
#             cv2.rectangle(img, (x1, y2-35),(x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name,(x1+6, y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255, 255),2)
#             #engine.say('Accepted')
#             #engine.runAndWait()
#     success1, img1 = cap1.read()
#     imgS1 = cv2.resize(img1, (0, 0), None, 0.25, 0.25)
#     imgS1 = cv2.cvtColor(imgS1, cv2.COLOR_BGR2RGB)
#
#     facesCurFrm1 = face_recognition.face_locations(imgS1)
#     encodesCurFrm1 = face_recognition.face_encodings(imgS1, facesCurFrm1)
#
#     for encodeFace1, faceLoc1 in zip(encodesCurFrm1, facesCurFrm1):
#         matches1 = face_recognition.compare_faces(encodeListKnown, encodeFace1)
#         faceDis1 = face_recognition.face_distance(encodeListKnown, encodeFace1)
#
#         matchIndex1 = np.argmin(faceDis1)
#
#         if matches1[matchIndex1] and min(faceDis1) <= 0.35:
#             name1 = (classNames[matchIndex1]).upper()
#             markAttendance1(name1)
#             y1, x2, y2, x1 = faceLoc1
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img1, (x1, y1), (x2, y2), (0, 255, 255), 2)
#             cv2.rectangle(img1, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img1, name1, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
#             #engine.say('Accepted')
#             #engine.runAndWait()
#     cv2.imshow('cam1', img1)
#     cv2.imshow('cam0', img)
#     cv2.waitKey(1)
#     if cv2.waitKey(1) & 0xFF == ord(' '):
#         break
#
# cap1.release()
# cap.release()
# cv2.destroyAllWindows()
