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

#Apply Bilinear
def applyBilinear(img, r_f, c_f):
    r, c = img.shape
    r_a =  math.floor(abs(r_f))
    c_a =  math.floor(abs(c_f))
    r_delta = r_f - r_a
    c_delta = c_f - c_a
    if(r_a < r-1 and c_a < c-1):
        pixel_value = (img[r_a, c_a]*(1-r_delta)*(1-c_delta)) + (img[r_a+1, c_a]*(r_delta)*(1-c_delta)) + (img[r_a, c_a+1]*(1 - r_delta)*(c_delta)) + (img[r_a+1, c_a+1]*(r_delta)*(c_delta))
    else:
        pixel_value = (img[r_a, c_a]*(1-r_delta)*(1-c_delta))
    return pixel_value

#Apply affine transformation
def applyAffineTranformation(img, r_, c_, affine_matrix):
    affine_matrix_inverse = np.linalg.inv(affine_matrix) 
    print(affine_matrix_inverse)
    r, c = img.shape
    new_img = np.zeros((r_,c_),dtype=np.uint8)
    for x_ in range(r_):
        for y_ in range(c_):
            x = affine_matrix_inverse[0,0]*x_ + affine_matrix_inverse[0,1]*y_ + affine_matrix_inverse[0,2]*1
            y = affine_matrix_inverse[1,0]*x_ + affine_matrix_inverse[1,1]*y_ + affine_matrix_inverse[1,2]*1
            w = affine_matrix_inverse[2,0]*x_ + affine_matrix_inverse[2,1]*y_ + affine_matrix_inverse[2,2]*1            
            x /= w
            y /= w
            #print(x, y, w)
            new_img[x_, y_] = applyBilinear(img, x, y)                      
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





