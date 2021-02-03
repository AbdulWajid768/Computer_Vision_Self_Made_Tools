import imageio as io
import matplotlib.pyplot as plt
import cv2 as cv


#img = cv.imread("earth.jpg", 0)
#img = cv.imread("flower.jpg", 0)
img = cv.imread("hand.jpg", 0)

#IMAGE RESIZING
#newImg = cv.resize(img, (100,100))

#CALUCULATING GLOBAL THRESHOLD
thresh, resImg1 = cv.threshold(img, 00, 1, cv.THRESH_BINARY+cv.THRESH_OTSU)


#CALCULATING ADAPTIVE THRESHOLD
resImg2 = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 99, 10)

#DISPLAY IMAGE THROUGH CV
# cv.imshow("Image", img)
# cv.waitKey()
# cv.destroyAllWindows()

plt.imshow(img, cmap="gray")
plt.show()

plt.imshow(resImg1, cmap="gray")
plt.show()

plt.imshow(resImg2, cmap="gray")
plt.show()

plt.close()