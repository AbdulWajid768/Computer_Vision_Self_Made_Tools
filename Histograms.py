import imageio as io
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv



#img = io.imread("hand.jpg" )
#img = io.imread("earth.jpg" )
img = io.imread("flower.jpg" )
img = img[:,:,0]

im1=cv.imread('earth.jpg',0)
new_im= cv.resize(im1,(100,100))
cv.imshow("new image", im1)
cv.waitKey(0)
cv.destroyAllWindows()


plt.imshow(img, cmap="gray")
plt.show()

plt.hist(img.ravel(), bins=100)
plt.show()

r, c = img.shape

newImg = np.zeros((r, c), dtype = np.uint8)

#T = 65 #hand
#T = 160 #earth
T = 140 #flower


for i in range(r):
    for j in range(c):
        if(img[i,j] <= T):
            newImg[i,j] = 0
        else:
            newImg[i,j] = 1
            

plt.imshow(newImg)
plt.show()
            
plt.close()