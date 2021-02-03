import matplotlib.pyplot as plt
import cv2 as cv
import random
import numpy as np


img = cv.imread("earth.jpg", 0)
#img = cv.imread("flower.jpg", 0)
#img = cv.imread("hand.jpg", 0)

r,c=img.shape

newImg = np.zeros((r , c) , dtype="uint8")

probNoise = 0.08

thresh = 1 - probNoise

for i in range(r):
    for j in range(c):
        ran = random.random()
        if ran < probNoise:
            newImg[i , j] = 0
        elif ran > thresh:
            newImg[i , j] = 255
        else:
            newImg[i, j] = img[i,j]
        

#DISPLAY IMAGE THROUGH CV
# cv.imshow("Image", img)
# cv.waitKey()
# cv.destroyAllWindows()



plt.imshow(img, cmap="gray")
plt.show()
plt.hist(img.ravel(), bins=100)
plt.show()

plt.imshow(newImg, cmap="gray")
plt.show()
plt.hist(newImg.ravel(), bins=100)
plt.show()
plt.close()