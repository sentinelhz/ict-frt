Jetson Nano base customized facial attendance edge device application and docker microservices.This code is the open source code for edge deployment of attendace kit built specifically for jetson nano with Gstreamer pipeline, Video capture buffer using CPython buffer and GIL , OpenCv LBHPrecognizer yml file that acts as the training model histogram for each user in a company.



########################################################################################################################################
Technology used :
OpenCV: (Opensource Computer Vision)(I m having cv2 version 4.5.1 built with cudann and CUDA compilation built on source with TensorRT, Keras, gstreamer spipeline which is  not availble on Jetpack 4.6 by default as OPENCV doesnt support gstreamer and cudalib.)
-Python(I am using Python 3.6.9)
-Default Jetpack 4.6
-Linux 4.9.253-tegra aarch64
-3.10.2
-v4l/v4l2:YES (linux/videodev2.h)
- Protobuf:build (3.5.1)
- NVIDIA CUDA:YES (ver 10.2, CUFFT CUBLAS FAST_MATH)
- NVIDIA GPU arch: 53
- cuDNN:YES (ver 8.2.1)
- Numpy :1.13
- GStreamer:YES (1.14.5)
- Parallel framework:TBB (ver 2020.2 interface 11102)
- FFMPEG Video I/O is also compiled.
- Bashrc has been updated with OPENBLAS_V8 ( check bashrc!)
- tkinter library for ICT UI
- PyQT5 for Crime Face recignition software.
- nvarguscamera gst pipeline 
- h.264 codec format video recording 
- docker damemon
- all the requirements are updated in the final-requirements.txt.
- Remember this project although is built for quick deployment of facial recognition, the authors bear no warranty of the code and may decline support to thsi version in near future, We welcome all open source enthusiasts to raise Pull requests on the repo which will be verified by the core team before being merged. Join us on sentinelhz.tech on their Dsicord channel for issues or raise git issues for bugs on the repo.

We couldnt have done this project without the open source community and hence would like to dedicate this working model to AI community worldwide.
Before proceeding with the project please kindly understand the problems faced by the core design team  especially in enabling the accelerated videobuffering and frame read using the nvarguscamera pipeline to create a faster video inferencing to meet the faster recogniton demand.

The follwing code and pipeline has been tested on 
OPENCV HARCASCADE XML
Dlib face recogniton
DeepFace API 
mtcnn TensorRT face-recogntion model
OpenCv dnn (SSD FaceNet)

We have found after repeated testing and speed inferencing using various face-recogniton models that OPENCV HARCASCADE and LBHPRecognizer to be the fastest among all the above with the specific gstreamer build.

We will coming soon with the container registry for all our docker microservices that connect to our online web platform built on Django Framework and deployed on AWS cloud.

Issues were faced by the design team in compiling the gstreamer and multithreading process for VideoCapture (src) assertion as queing frames for processing were leading to the crashing of the camera board.



#########################################################################################################################################
How it works :

When we run train.py a window is opened and ask for entering Id and Enter Name. After entering name and id then we have to click Take Images button. By clicking Take Images camera of running computer is opened and it starts taking an image sample of the person. This Id and Name is stored in folder StudentDetails and the file name is StudentDetails.csv. It takes 60 images as a sample and stores them in folder TrainingImage.After completion, it notifies that images saved.
After taking the image sample we have to click Train Image button. Now it takes few seconds to train machine for the images that are taken by clicking Take Image button and creates a Trainner.yml file and store in TrainingImageLabel folder.
Now all initial setups are done. By clicking the Track Image button camera of running machine is opened again. If the face is recognised by the system then Id and Name of person is shown on Image. Press Q(or q) for quit this window. After quitting it attendance of person will be stored in Attendance folder as CSV file with name, id, date and time and it is also available in the window.


########################################################################################################################################

How to install opencv
 -->   pip3 install opencv-contrib-python


How to install tkinter GUI interface
 --> sudo apt-get install python3-tk

#########################################################################################################################################
Train Recognizer
OpenCV provides three methods of face recognition:
Eigenfaces
Fisherfaces
Local Binary Patterns Histograms (LBPH)
Eigenfaces and Fisherfaces find a mathematical description of the most dominant features of the training set as a whole. LBPH analyzes each face in the training set separately and independently. The LBPH method is somewhat simpler, in the sense that we characterize each image in the dataset locally; and when a new unknown image is provided, we perform the same analysis on it and compare the result to each of the images in the dataset. We will be using the LBPH Face recognizer for our purpose.


For more understanding of LBH Recognizer please  refer " https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b "

thanks:
Kunal Kaushik, a digital builder who is always learning and building.
Master developer of this repo.
Waiting for your contribution.
