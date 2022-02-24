# Vision-based-waste-sorting
Waste separation is an important step in the recycling process to preserve the environment.
In this project we sort waste using a camera avec a Convolutional Neural Network.
## Idea
The idea is to build a **vision-based waste sorting machine**.
This machine consists of:
* A treadmill (tapis roulant);
* A camera;
* A robot arm (bras robot);
* A computer with a GPU graphics card for image processing.
## Process diagram
![image](https://user-images.githubusercontent.com/42723115/155526710-b02fec71-6785-4266-905e-c849e1e22fba.png)
* The waste passes on the treadmill under the camera.
![image](https://user-images.githubusercontent.com/42723115/155526850-818a6d1e-9f25-4375-85a7-10e59bd0321f.png)
* The camera sends the images to the computer.
![image](https://user-images.githubusercontent.com/42723115/155526938-6ba32b6a-89fc-455e-abac-e2a329e76ab7.png)
* The computer uses Artificial Intelligence techniques to:
    - Detecting objects
    - Recognizing objects.
## Some examples of object detection
![image](https://user-images.githubusercontent.com/42723115/155527584-4b4ff806-c87c-4be5-82f7-aa581df570ca.png)
## Why not learning using a database of waste images?
![image](https://user-images.githubusercontent.com/42723115/155527673-6f0b6c57-8660-4ebf-b397-23c2836eba21.png)
## After detecting and recognizing objects
* The computer sends a signal to the robot arm with the object's coordinates (x, y).
* The robot arm picks up the object and places it in a container.
![image](https://user-images.githubusercontent.com/42723115/155527811-bde6c896-bd20-4d37-aece-9bd115e1bb91.png)
