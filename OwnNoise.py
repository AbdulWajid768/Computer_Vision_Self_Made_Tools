import numpy as np
import random
import imageio as io
import cv2 as cv
import matplotlib.pyplot as plt



def getPixelValue(img, i, j, r, c):
    value = 0
    for k in range(i-1, i+2):
        for l in range (j-1, j+2):
            if((k>=0 and k<r) and (l>=0 and l<c)):
                value += img[l][j]
    
    value /= 7
    value %= 255
    return value
            

def meanNoise(img, prob):
    r, c = img.shape
    newImg = np.zeros((r,c), dtype="uint8")
    for i in range(r):
        for j in range(c):
            rand = random.random()
            if rand < prob:
                newImg[i][j] = getPixelValue(img, i, j, r, c)
            else:
                newImg[i][j] = img[i][j]
    return newImg
            


img = cv.imread("rough.jpg", 0)

noiseImg = meanNoise(img, 0.01)
#noiseImg.astype("uint8")

plt.imshow(img, cmap = "gray")
plt.show()

plt.imshow(noiseImg, cmap = "gray")
plt.show()

plt.close()


