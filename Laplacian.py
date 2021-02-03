import numpy as np
import random
import imageio as io
import cv2 as cv
import matplotlib.pyplot as plt
import math


mask1 = np.array([[0,-1,0],
                  [-1,4,-1],
                  [0,-1,0]])


mask2 = np.array([[-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]])






def getPixelValue(img, M, i, j, r_img, c_img, r_mask, c_mask):
    value = 0
    for k in range(i-int(r_mask/2), i+int(r_mask/2) + 1):
        for l in range (j-int(c_mask/2), j+int(c_mask/2)+1):
            if((k>=0 and k<r_img) and (l>=0 and l<c_img)):
                value = value + int(img[k][l]*M[k-i+int(r_mask/2)][l-j+int(c_mask/2)])
    return int(value)


def applyMask(img, mask):
    r_img, c_img = img.shape
    r_mask, c_mask = mask.shape
    new_img = np.zeros((r_img, c_img), dtype="int32")
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = getPixelValue(img, mask, i, j, r_img, c_img, r_mask, c_mask)
    #return scaleImage(new_img, 255)
    return new_img

def scaleImage(img, maxVal):
    r_img, c_img = img.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    img_minVal = img.min()
    img_maxVal = img.max()

    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = int((img[i][j] - img_minVal)*maxVal/(img_maxVal-img_minVal))
    return new_img
    

def applyLaplacianFilter(img, mask):
    r_img, c_img = img.shape
    new_img = np.zeros((r_img, c_img), dtype="int32")
    maskImg = applyMask(img, mask)
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = math.sqrt( maskImg[i][j]**2)
            #print(new_img[i][j] , maskImg[i][j])
    return scaleImage(new_img, 255)
    #return new_img    

   




img = cv.imread("img.png", 0)

resImg1 = applyLaplacianFilter(img, mask1)
resImg2 = applyLaplacianFilter(img, mask2)

plt.imshow(img, cmap = "gray")
plt.show()

plt.imshow(resImg1, cmap = "gray")
plt.show()

plt.imshow(resImg2, cmap = "gray")
plt.show()



plt.close()


