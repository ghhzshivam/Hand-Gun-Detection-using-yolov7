# Hand-Gun-Detection-using-yolov7
Detecting the  handguns from the images using custom data set of handgun annotated images.

## Problem: There are many crimes taking place in the city so to detect the handgun from the camera for security resons.

## Dataset:
The dataset is of Images with handguns with annotated labels. The dataset is 3479 training images and 480 val images. There are two different files with immages and labels.

##Yolov7 
 Yolov7 is downloaded form https://github.com/WongKinYiu/yolov7 and the custom dataset of handguns are added. Then the model is trained based on the custom dataset the classes.

![yolov7result-1024x763](https://user-images.githubusercontent.com/45498501/189310033-235af5f0-7ad3-43ed-9fd1-bfd89d8bbcc1.png)


For Demon of the model. We can see that the person is standing with a handgun in is hand

![1](https://user-images.githubusercontent.com/45498501/189306783-043b08fd-6426-467d-93ff-ea155a77a406.jpg)

After the Yolov7 model is trained on the handgun images for 100 epochs the results are

![1pred](https://user-images.githubusercontent.com/45498501/189307428-bf017cb3-7467-4f62-9ca5-e8b1b8658852.jpg)
