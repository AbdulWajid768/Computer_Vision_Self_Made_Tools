import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math


# l = 0
#     m = 0
#     for i in range(r):
#         m=0
#         for j in range(c):
#             if(l < r_new and m < c_new):
#                 #print(l,m)
#                 new_img[l,m] = img[i,j]
#             m+=x
#         l+=x



def applyInterpolation(img, x):
    if(x==0):
        return img
    elif(x>0):
        return largeImageByX(img, x)
    else:
        return smallImageByX(img, abs(x))
    

def largeImageByX(img, x):
    r, c = img.shape
    new_img = np.zeros((r*x, c*x), dtype=np.uint8)
    r_new, c_new = new_img.shape
    Sr = r/r_new
    Sc = c/c_new
    for i in range(r_new):
        for j in range(c_new):
            new_i = math.floor(Sr*i)
            new_j = math.floor(Sc*j)
            new_img[i,j] = img[new_i, new_j]   
    return new_img



def smallImageByX(img, x):
    r, c = img.shape
    new_img = np.zeros((round(r/x), round(c/x)), dtype=np.uint8)
    r_new, c_new = new_img.shape
    Sr = round((r-1)/r_new)
    Sc = round((c-1)/c_new)
    for i in range(r_new):
        for j in range(c_new):
            new_i = math.floor(Sr*i)
            new_j = math.floor(Sc*j)
            new_img[i,j] = img[new_i, new_j]   
    return new_img


#img = cv.imread("img.png", 0)
img = cv.imread("earth.jpg", 0)
plt.imshow(img, cmap = "gray")
plt.show()

resized_img = applyInterpolation(img, 2)
plt.imshow(resized_img, cmap = "gray")
plt.show()



plt.close()


