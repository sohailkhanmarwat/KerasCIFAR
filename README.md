# CIFAR Keras

Based on [EN10 CIFAR](https://github.com/EN10/CIFAR)

The CIFAR-10 dataset consists of 60000 32x32 colour images in [10 classes](https://github.com/EN10/KerasCIFAR#classes), with 6000 images per class.  
There are 50000 training images and 10000 test images.  
The dataset is divided into five training batches and one test batch, each with 10000 images.

[load_cifar.py](https://github.com/EN10/KerasCIFAR/blob/master/load_cifar.py):
* download and extract CIFAR.
* load batch into array
* test train split
* load images of classid

## Install Tensorflow

    sudo pip install -U pip
    sudo pip install tensorflow 

## Run

    python keras.py
    
### Classes:

0 : airplane  
1 : automobile  
2 : bird  
3 : cat  
4 : deer  
5 : dog  
6 : frog  
7 : horse  
8 : ship  
9 : truck 