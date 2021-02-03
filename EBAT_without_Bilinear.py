import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import math

#points before and after transformation

x1 = 0
y1 = 0
x1_ = 0
y1_ = 719

x2 = 0
y2 = 2399
x2_ = 719
y2_ = 719

x3 = 2399
y3 = 2399
x3_ = 719
y3_ = 0


#Matrix A
A_matrix = np.array([[x1,y1,1,0,0,0],
                     [0,0,0,x1,y1,1],
                     [x2,y2,1,0,0,0],
                     [0,0,0,x2,y2,1],
                     [x3,y3,1,0,0,0],
                     [0,0,0,x3,y3,1]])

#Matrix b
b_matrix = np.array([[x1_],
                     [y1_],
                     [x2_],
                     [y2_],
                     [x3_],
                     [y3_]])

#Calculate the affine transformation
def getAffineMatrix(A, b):
    A_1 = np.linalg.inv(A) 
    x = np.dot(A_1,b)
    AM = np.reshape(x, (2,3))
    AM = np.concatenate((AM, np.array([[0,0,1]])), axis=0)
    #AM = AM.astype('int32') 
    print("\nAffine matrix = \n",AM)
    return AM


#Apply affine transformation
def applyAffineTranformation(img, r_, c_, affine_matrix):
    r, c = img.shape
    new_img = np.zeros((r_,c_),dtype=np.uint8)
    for x in range(r):
        for y in range(c):
            x_ = affine_matrix[0,0]*x + affine_matrix[0,1]*y + affine_matrix[0,2]*1
            y_ = affine_matrix[1,0]*x + affine_matrix[1,1]*y + affine_matrix[1,2]*1
            w_ = affine_matrix[2,0]*x + affine_matrix[2,1]*y + affine_matrix[2,2]*1            
            x_ /= w_
            y_ /= w_
            new_img[math.floor(x_),math.floor(y_)] = img[x,y]                   
    return new_img
    

#Original Image
img1 = cv.imread("Image_1.jpg", 0)
plt.imshow(img1, cmap = "gray")
plt.show() 

#Transformed Image
img2 = cv.imread("Image1_Transformed.jpg", 0)
plt.imshow(img2, cmap = "gray")
plt.show()

#Affine Matrix
affine_matrix = getAffineMatrix(A_matrix, b_matrix)

#Row, Col of Transformed Image
r_, c_ = img2.shape

#Image after applying affine Tranformation
res_img = applyAffineTranformation(img1, r_, c_, affine_matrix)
plt.imshow(res_img, cmap = "gray")
plt.show()





