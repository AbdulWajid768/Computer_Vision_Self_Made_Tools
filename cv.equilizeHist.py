import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("flower.jpg", 0)


newImg = cv.equalizeHist(img)


plt.imshow(img, cmap="gray")
plt.show()


plt.imshow(newImg, cmap="gray")
plt.show()

plt.close()
