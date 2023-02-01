<div id="header" align="center">
  <img src="https://user-images.githubusercontent.com/68182283/215999231-cd4e0bb8-b3d7-4ef8-98d8-3ae617481188.png" width="350"/>
</div>

# Introduction
CoCe :robot: is a deep learning-based project aiming to classify images out of the following 10 classes:
* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

CoCe was built as part of the EASS course in order to get an understanding of how to deploy an end-to-end application using various tools commonly used in the tech industry.

# Demonstration
https://user-images.githubusercontent.com/68182283/215993391-bb095f79-2d3a-4f56-bc0d-aeb70c3acfaa.mp4

# Architecture
![image](https://user-images.githubusercontent.com/68182283/213872894-281fcbb6-b20d-4605-9b13-19b7a7017d52.png)

# Performance
Due to computational restrictions, the neural network was not able to go through many epochs. Nevertheless, the neural network gain pretty good accuracy score and the loss was minimized as much as possible so the neural network did not went to overfit.

* Accuracy: 43.25% -> 76.15%
* Loss: 1.5687 -> 0.6955

# Deployment
First of all you will need Git and Docker installed on your machine.

1. Open the Terminal, go inside your desired folder and run the following command:
``` bash
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/CoCe.git
```
2. Then you will have to go inside the "CoCe" folder using the following command:
```bash
cd CoCe
```
3. To run CoCe, you will have to enter the following command:
```bash
docker-compose up
```
4. Congratulations! You may access CoCe via your browser by typing the following address:
```bash
http://localhost:8501/
```  
