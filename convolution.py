import numpy as np
import random
import imageio as io
import cv2 as cv
import matplotlib.pyplot as plt

#con_mask = [[8,1,6],[3,5,7],[4,9,2]]

con_mask = np.zeros((3,3) , dtype="uint8")

con_mask[0] = [8,1,6]
con_mask[1] = [3,5,7]
con_mask[2] = [4,9,2]

def rotateMask180Degree(con_mask):
    r, c = con_mask.shape
    for i in range(int(r/2)):
        for j in range(c):
            temp = con_mask[i][j]
            con_mask[i][j] =  con_mask[r-1-i][j] 
            con_mask[r-1-i][j] = temp;
    for i in range(r):
        for j in range(int(c/2)):
            temp = con_mask[i][j]
            con_mask[i][j] =  con_mask[i][c-1-j]
            con_mask[i][c-1-j] = temp;
    return con_mask


def getPixelValue(img, con_mask, i, j, r_img, c_img, r_mask, c_mask):
    value = 0
    for k in range(i-int(r_mask/2), i+int(r_mask/2) + 1):
        for l in range (j-int(c_mask/2), j+int(c_mask/2)+1):
            if((k>=0 and k<r_img) and (l>=0 and l<c_img)):
                value = value + img[k][l]*con_mask[k-i+int(r_mask/2)][l-j+int(c_mask/2)]
    return int(value)


def convolutionImg(img, con_mask):
    r_img, c_img = img.shape
    con_mask = rotateMask180Degree(con_mask)
    r_mask, c_mask = con_mask.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = getPixelValue(img, con_mask, i, j, r_img, c_img, r_mask, c_mask)
    return new_img
    
   




img = cv.imread("rough.jpg", 0)

plt.imshow(img, cmap = "gray")
plt.show()

con_img = convolutionImg(img, con_mask)

plt.imshow(con_img, cmap = "gray")
plt.show()

plt.close()


