# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
import PIL
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import requests, os, re
from pathlib import Path

window = tk.Tk()
window.title("Sentinel-EYE")
window.configure(background ='#fcf7df')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
img = ImageTk.PhotoImage(Image.open("profile.jpg"))
panel = tk.Label(window, image = img)
panel.pack(side = "left", fill = "y", expand = "no")

message = tk.Label(
    window, text ="Sentinel-EYE",
    bg ="#5ccdeb", fg = "black", width = 50,
    height = 3, font = ('helvetica', 30, 'bold'))
     
message.place(x = 100, y = 20)
 
lbl = tk.Label(window, text = "Id",
width = 20, height = 2, fg ="red",
bg = "white", font = ('arial', 15, ' bold ') )
lbl.place(x = 400, y = 200)
 
txt = tk.Entry(window,
width = 20, bg ="white",
fg ="red", font = ('times', 15, ' bold '))
txt.place(x = 700, y = 215)
 
lbl2 = tk.Label(window, text ="Name",
width = 20, fg ="red", bg ="white",
height = 2, font =('times', 15, ' bold '))
lbl2.place(x = 400, y = 300)
 
txt2 = tk.Entry(window, width = 20,
bg ="white", fg ="red",
font = ('times', 15, ' bold ')  )
txt2.place(x = 700, y = 315)
window.attributes('-alpha', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)



#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open("profile.jpg"))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("profile.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)







def get_jetson_gstreamer_source(capture_width=1280, capture_height=720, display_width=640, display_height=480, framerate=60, flip_method=0):
    """
    Return an OpenCV-compatible video source description that uses gstreamer to capture video from the camera on a Jetson Nano
    """
    return (
            f'nvarguscamerasrc ! video/x-raw(memory:NVMM), ' +
            f'width=(int){capture_width}, height=(int){capture_height}, ' +
            f'format=(string)NV12, framerate=(fraction){framerate}/1 ! ' +
            f'nvvidconv flip-method={flip_method} ! ' +
            f'video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)BGRx ! ' +
            'videoconvert ! video/x-raw, format=(string)BGR ! appsink'
            )







def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def markAttendance(str):
    file_exists = os.path.isfile('Attendance.csv')
    with open('Attendance.csv','a') as f:
        if not file_exists:
            myDataList = f.readlines()
            Id =[]
            nameList = []

            for line in myDataList:
              entry = line.split(',')
              nameList.append(entry[0])
            if name not in nameList:
                 now = datetime.datetime.now()
                 dtString = now.strftime('%H:%M:%S')
                 f.writelines(f'{Id}\n{name},{dtString}')
        else:
          with open('Attendance.csv','w') as f:
             Id =[]
             nameList = []
        
             now = datetime.datetime.now()
             dtString = now.strftime('%H:%M:%S')
             f.writelines(f'\n{Id},{name},{dtString}')
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(get_jetson_gstreamer_source(), cv2.CAP_GSTREAMER)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage/ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails/StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)    
    df=pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(get_jetson_gstreamer_source(), cv2.CAP_GSTREAMER)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    ts = time.time()
    json_to_export ={}

    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-"+aa
                print(tt)
                name = tt
                json_to_export['name'] = f'{name}'
                json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_mday}'
                json_to_export['date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'
               # json_to_export['picture_array'] = frame.tolist()


                ###Send request to API ##
                r = requests.post(url='	https://webhook.site/3206245e-73a9-4f7b-9249-cebbf8b1df36',json = json_to_export)
                print("Status: ",r.status_code)
               #markAttendance(tt)
                
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    #ts = time.time()      
    #date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    #timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    #Hour,Minute,Second=timeStamp.split(":")
    #fileName="Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    #attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res="Hello Attendance Marked"
    message2.configure(text= res)


takeImg = tk.Button(window, text ="TakeImages",
command = TakeImages, fg ="white", bg ="green",
width = 20, height = 3, activebackground = "Red",
font =('times', 15, ' bold '))
takeImg.place(x = 200, y = 500)
trainImg = tk.Button(window, text ="TrainImages",
command = TrainImages, fg ="white", bg ="green",
width = 20, height = 3, activebackground = "Red",
font =('times', 15, ' bold '))
trainImg.place(x = 500, y = 500)
trackImg = tk.Button(window, text ="Track",
command = TrackImages, fg ="white", bg ="green",
width = 20, height = 3, activebackground = "Red",
font =('times', 15, ' bold '))
trackImg.place(x = 800, y = 500)
quitWindow = tk.Button(window, text ="Quit",
command = window.destroy, fg ="white", bg ="green",
width = 20, height = 3, activebackground = "Red",
font =('times', 15, ' bold '))
quitWindow.place(x = 1100, y = 500)
 
window.mainloop()
