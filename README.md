<div id="header" align="center">
  <img src="https://media.giphy.com/media/VW4VROUnMdKaTODi9u/giphy.gif" width="200"/>
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

# Performance
Due to computational restrictions, the neural network was not able to go through many epochs. Nevertheless, the neural network gain pretty good accuracy score and the loss was minimized as much as possible so the neural network did not went to overfit.

* Accuracy: 43.25% -> 76.15%
* Loss: 1.5687 -> 0.6955

# Architecture
![image](https://user-images.githubusercontent.com/68182283/213871868-825d794d-09d6-4133-b58c-c888c7d45f29.png)

# 🌱 Deployment
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
