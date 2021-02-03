import numpy as np
import random
import imageio as io
import cv2 as cv
import matplotlib.pyplot as plt
import math

Mx = np.zeros((3,3))
My = np.zeros((3,3))

sobel = np.array([[1,0,-1000],
                  [1,0,-1],
                  [1,0,-1]])

Mx[0] = [1,0,-1]
Mx[1] = [1,0,-1]
Mx[2] = [1,0,-1]

My[0] = [1,1,1]
My[1] = [0,0,0]
My[2] = [-1,-1,-1]




def getPixelValue(img, M, i, j, r_img, c_img, r_mask, c_mask):
    value = 0
    for k in range(i-int(r_mask/2), i+int(r_mask/2) + 1):
        for l in range (j-int(c_mask/2), j+int(c_mask/2)+1):
            if((k>=0 and k<r_img) and (l>=0 and l<c_img)):
                value = value + int(img[k][l]*M[k-i+int(r_mask/2)][l-j+int(c_mask/2)])
    return int(value)


def applyMx(img, Mx):
    r_img, c_img = img.shape
    r_mask, c_mask = Mx.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = getPixelValue(img, Mx, i, j, r_img, c_img, r_mask, c_mask)
    return new_img

def applyMy(img, My):
    r_img, c_img = img.shape
    r_mask, c_mask = My.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = getPixelValue(img, My, i, j, r_img, c_img, r_mask, c_mask)
    return new_img

def applyMxAndMy(img, Mx, My):
    r_img, c_img = img.shape
    imgMx = np.zeros((r_img, c_img), dtype="uint8")
    imgMy = np.zeros((r_img, c_img), dtype="uint8")
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    imgMx = applyMx(img, Mx)
    imgMy = applyMy(img, My)
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = math.sqrt( imgMx[i][j]**2  +  imgMy[i][j]**2)
    return new_img
    

   




#img = cv.imread("earth.jpg", 0)
img = cv.imread("nobita.png", 0)
imgMx = applyMx(img, Mx)
imgMy = applyMy(img, My)
imgMxy = applyMxAndMy(img, Mx, My)

plt.imshow(img, cmap = "gray")
plt.show()
plt.imshow(imgMx, cmap = "gray")
plt.show()
plt.imshow(imgMy, cmap = "gray")
plt.show()
plt.imshow(imgMxy, cmap = "gray")
plt.show()





plt.close()


