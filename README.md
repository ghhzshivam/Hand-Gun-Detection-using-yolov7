# Hand-Gun-Detection-using-yolov7
Detecting the handguns from the images using custom data set of handgun annotated images.

## Problem:
There is a increase in gun voilence many crimes taking place in the city so detect the handgun from the camera photage.

## Dataset:
The dataset is containg images with handguns and annotated labels. The dataset is 3479 training images and 480 val images. There are two different files with immages and labels. Below tis the following example of the images where we can see a person having a handgun in a street. The size of images is (640,640).
![1](https://user-images.githubusercontent.com/45498501/189306783-043b08fd-6426-467d-93ff-ea155a77a406.jpg)

## Yolov7:
Yolov7 is the latest verion and has performed better than other object detection models. Yolov7 is downloaded form https://github.com/WongKinYiu/yolov7 and the custom dataset of handguns are added to customise the model to detect handguns only.

![yolov7result-1024x763](https://user-images.githubusercontent.com/45498501/189310033-235af5f0-7ad3-43ed-9fd1-bfd89d8bbcc1.png)

## Result:
After the Yolov7 model is trained on the handgun images for 100 epochs the model is able to detect handguns.

![1pred](https://user-images.githubusercontent.com/45498501/189307428-bf017cb3-7467-4f62-9ca5-e8b1b8658852.jpg)
