import numpy as np
import random
import cv2 as cv
import matplotlib.pyplot as plt


def addSaltPepperNoise(img, prob):
    thresh = 1 - prob
    r, c = img.shape
    newImg = np.zeros((r,c) , dtype="uint8")

    for i in range(r):
        for j in range(c):
            ran = random.random()
            if ran < prob:
                newImg[i , j] = 0
            elif ran > thresh:
                newImg[i , j] = 255
            else:
                newImg[i, j] = img[i,j]
    return newImg



def getPixelValue(img, i, j, img_row, img_col, win_row, win_col):
    window = np.zeros(win_row*win_col , dtype="uint8")
    index = 0
    for l in range(i-1, i+ int(win_row/2) + 1):
        for m in range(j-1, j + int(win_col/2) + 1):
            if((l>0 and l<img_row) and (m>0 and m<img_col)):
                window[index] = img[l][m]
            else:
                window[index] = 0
            index += 1
    return np.median(window)
            


def applyMedianFilter(img, win_row, win_col):
    r, c = img.shape
    newImg = np.zeros((r, c), dtype="uint8")
    for i in range(r):
        for j in range(c):
            newImg[i][j] = getPixelValue(img,i, j, r, c, win_row, win_col)
            
    return newImg
    
   




img = cv.imread("rough.jpg", 0)

plt.imshow(img, cmap = "gray")
plt.show()

noiseImg = addSaltPepperNoise(img, 0.01)

plt.imshow(noiseImg, cmap = "gray")
plt.show()

medianImg = applyMedianFilter(noiseImg, 3, 3)
plt.imshow(medianImg, cmap = "gray")
plt.show()

medianImg = applyMedianFilter(noiseImg, 3, 3)
plt.imshow(medianImg, cmap = "gray")
plt.show()

medianImg = applyMedianFilter(noiseImg, 3, 3)
plt.imshow(medianImg, cmap = "gray")
plt.show()

medianImg = applyMedianFilter(noiseImg, 3, 3)
plt.imshow(medianImg, cmap = "gray")
plt.show()

plt.close()


