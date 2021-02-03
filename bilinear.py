import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math




def applyBilinear(img, x):
    if(x==0):
        return img
    elif(x>0):
        return largeImageByX(img, x)
    else:
        return smallImageByX(img, abs(x))
    

def largeImageByX(img, x):
    r, c = img.shape
    new_img = np.zeros((r*x, c*x), dtype=np.uint8)
    R, C = new_img.shape
    Sr = r/R
    Sc = c/C
    for i in range(R):
        for j in range(C):
            r_f = Sr*i
            c_f = Sc*j
            r_a =  math.floor(abs(r_f))
            c_a =  math.floor(abs(c_f))
            r_delta = r_f - r_a
            c_delta = c_f - c_a
            if(r_a < r-1 and c_a < c-1):
                new_img[i,j] = (img[r_a, c_a]*(1-r_delta)*(1-c_delta)) + (img[r_a+1, c_a]*(r_delta)*(1-c_delta)) + (img[r_a, c_a+1]*(1 - r_delta)*(c_delta)) + (img[r_a+1, c_a+1]*(r_delta)*(c_delta))
            else:
                new_img[i,j] = (img[r_a, c_a]*(1-r_delta)*(1-c_delta))

    return new_img



def smallImageByX(img, x):
    r, c = img.shape
    new_img = np.zeros((round(r/x), round(c/x)), dtype=np.uint8)
    R, C = new_img.shape
    Sr = round((r-1)/R)
    Sc = round((c-1)/C)
    for i in range(R):
        for j in range(C):
            r_f = Sr*i
            c_f = Sc*j
            r_a = round(abs(r_f))
            c_a = round(abs(c_f))
            r_delta = r_f - r_a
            c_delta = c_f  -c_a        
            new_img[i,j] = (img[r_a, c_a]*(1-r_delta)*(1-c_delta)) + (img[r_a+1, c_a]*(r_delta)*(1-c_delta)) + (img[r_a, c_a+1]*(1 - r_delta)*(c_delta)) + (img[r_a+1, c_a+1]*(r_delta)*(c_delta))
    return new_img



#img = cv.imread("img.png", 0)
img = cv.imread("earth.jpg", 0)
plt.imshow(img, cmap = "gray")
plt.show()

resized_img = applyBilinear(img, 2)
plt.imshow(resized_img, cmap = "gray")
plt.show()



plt.close()


