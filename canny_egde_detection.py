import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math










def scaleImage(img, maxVal):
    r_img, c_img = img.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    img_minVal = img.min()
    img_maxVal = img.max()

    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = int((img[i][j] - img_minVal)*maxVal/(img_maxVal-img_minVal))
    return new_img


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

def applyGaussianBlur(img):
    mask = np.array([[1,2,1],[2,4,2],[1,2,1]])
    new_img = applyMask(img, mask)
    return scaleImage(new_img, 255)
    #return new_img
    
def gradientCalculation(img):
    Kx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    Ky = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

    r_img, c_img = img.shape
    new_img = np.zeros((r_img, c_img), dtype="int32")
    imgKx = applyMask(img, Kx)
    imgKy = applyMask(img, Ky)
    theeta = np.arctan2(imgKy, imgKx)
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = math.sqrt( imgKx[i][j]**2  +  imgKy[i][j]**2)
    return (scaleImage(new_img, 255), theeta*180.0/np.pi)


def nonMaxSuppression(img, theeta):
    rows, cols = img.shape
    new_img = np.zeros((rows,cols), dtype="uint8")
    theeta[theeta < 0] += 180

    for i in range(1,rows-1):
        for j in range(1,cols-1):
            right = 255
            left = 255
                
            #angle 0
            if (0 <= theeta[i,j] < 22.5) or (157.5 <= theeta[i,j] <= 180):
                right = img[i, j+1]
                left = img[i, j-1]
                
            #angle 45
            elif (22.5 <= theeta[i,j] < 67.5):
                right = img[i+1, j-1]
                left = img[i-1, j+1]
                
            #angle 90
            elif (67.5 <= theeta[i,j] < 112.5):
                right = img[i+1, j]
                left = img[i-1, j]
                
            #angle 135
            elif (112.5 <= theeta[i,j] < 157.5):
                right = img[i-1, j-1]
                left = img[i+1, j+1]

            if (img[i,j] >= right) and (img[i,j] >= left):
                new_img[i,j] = img[i,j]
            else:
                new_img[i,j] = 0
                    
    return new_img  

def doubleThreshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.095, weak=25, strong=255):
    highThreshold = int(img.max() * highThresholdRatio);
    lowThreshold = int(highThreshold * lowThresholdRatio);
    print(highThreshold, lowThreshold)
    rows, cols = img.shape
    new_img = np.zeros((rows,cols), dtype="uint8")

    for i in range(1,rows-1):
            for j in range(1,cols-1):
                if(img[i][j] > highThreshold):
                    new_img[i][j] = strong
                elif(img[i][j] < lowThreshold):
                    new_img[i][j] = 0
                else:
                    new_img[i][j] = weak

    return (new_img, weak, strong)


def edgeTrackingHysteresis(img, weak=25, strong=255):
    rows, cols = img.shape
    new_img = np.zeros((rows,cols), dtype="uint8")
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if (img[i,j] == weak):
                if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                    or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                    or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):                       
                    new_img[i, j] = strong
                else:
                    new_img[i, j] = 0
    return new_img







img = cv.imread("img.png", 0)
#img = cv.imread("earth.jpg", 0)
plt.imshow(img, cmap = "gray")
plt.show()

resImg1 = applyGaussianBlur(img)
plt.imshow(resImg1, cmap = "gray")
plt.show()

resImg2, theeta = gradientCalculation(resImg1)
plt.imshow(resImg2, cmap = "gray")
plt.show()

resImg3 = nonMaxSuppression(resImg2, theeta)
plt.imshow(resImg3, cmap = "gray")
plt.show()

resImg4, strong, weak = doubleThreshold(resImg3)
plt.imshow(resImg4, cmap = "gray")
plt.show()

resImg5 = edgeTrackingHysteresis(resImg4)
plt.imshow(resImg5, cmap = "gray")
plt.show()




plt.close()


