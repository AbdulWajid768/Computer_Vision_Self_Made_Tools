import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math

def makePatch(img, i, j, r_img, c_img, r_patch, c_patch):
    patch = np.zeros((r_patch*c_patch), dtype="uint8")
    m = 0;
    for k in range(i-int(r_patch/2), i+int(r_patch/2) + 1):
        for l in range (j-int(c_patch/2), j+int(c_patch/2)+1):
            if((k>=0 and k<r_img) and (l>=0 and l<c_img)):
                patch[m] = img[k][l]
            m+=1
    return patch



def computeMeanAtPatch(patch):
    return np.sum(patch)/patch.size

def computeMedianAtPatch(patch):
    patch = np.sort(patch)
    return patch[round((patch.size+1)/2)]

def computeVarianceAtPatch(patch, mean):
    values = 0
    for i in range(patch.size):
        values+=(patch[i]-mean)**2
    return values/(patch.size-1)

def computeStandardDeviation(variance):
    return math.sqrt(variance)

def computeSkewnessAtPatch(patch, mean, std_deviation):
    values = 0
    for i in range(patch.size):
        values+=((patch[i]-mean)/std_deviation)**3
    return values/ patch.size

def computeKurtosisAtPatch(patch, mean, std_deviation):
    values = 0
    for i in range(patch.size):
        values += ((patch[i]-mean)/std_deviation)**4
    return values/patch.size

def computeMeanAbsoluteDeviationAtPatch(patch, mean):
    values = 0
    for i in range(patch.size):
        values += abs(patch[i]-mean)
    return values/patch.size

def computeMedianAbsoluteDeviationAtPatch(patch, mead):
    patch = patch - mead
    return patch[round((patch.size+1)/2)]

def computeLocalContrastAtPatch(patch, mean):
    return patch.max() - patch.min() 

def computeLocalProbabiltyAtPatch(patch, k):
    return np.count_nonzero(patch == k)/patch.size

def computep25AtPatch(patch):
    patch = np.sort(patch)
    return patch[round(patch.size*0.25)]

def computep75AtPatch(patch):
    patch = np.sort(patch)
    return patch[round(patch.size*0.27)]

def scaleImage(img, maxVal):
    r_img, c_img = img.shape
    new_img = np.zeros((r_img, c_img), dtype="uint8")
    img_minVal = img.min()
    img_maxVal = img.max()

    for i in range(r_img):
        for j in range(c_img):
            new_img[i][j] = int((img[i][j] - img_minVal)*maxVal/(img_maxVal-img_minVal))
    return new_img
    




def computeFOSF(img, r_patch, c_patch):
    r_img, c_img = img.shape
    mean = np.zeros((r_img, c_img), dtype="int32")
    median = np.zeros((r_img, c_img), dtype="int32")
    variance = np.zeros((r_img, c_img), dtype="int32")
    standard_deviation = np.zeros((r_img, c_img), dtype="int32")
    skewness = np.zeros((r_img, c_img), dtype="int32")
    kurtosis = np.zeros((r_img, c_img), dtype="int32")
    mean_absolute_deviation = np.zeros((r_img, c_img), dtype="int32")
    median__absolute_deviation = np.zeros((r_img, c_img), dtype="int32")
    local_contrast = np.zeros((r_img, c_img), dtype="int32")
    local_probability = np.zeros((r_img, c_img), dtype="int32")
    p25 = np.zeros((r_img, c_img), dtype="int32")
    p75 = np.zeros((r_img, c_img), dtype="int32")
    for i in range(r_img):
        for j in range(c_img):
            patch = makePatch(img, i, j, r_img, c_img,  r_patch, c_patch)   
            mean[i][j] = computeMeanAtPatch(patch)
            median[i][j] = computeMedianAtPatch(patch)
            variance[i][j] = computeVarianceAtPatch(patch, mean[i][j])
            standard_deviation[i][j] = computeStandardDeviation(variance[i][j])
            skewness[i][j] = computeSkewnessAtPatch(patch, mean[i][j], standard_deviation[i][j])
            kurtosis[i][j] = computeKurtosisAtPatch(patch, mean[i][j], standard_deviation[i][j])
            mean_absolute_deviation[i][j] = computeMeanAbsoluteDeviationAtPatch(patch, mean[i][j])
            median__absolute_deviation[i][j] = computeMedianAbsoluteDeviationAtPatch(patch, median[i][j])
            local_contrast[i][j] = computeLocalContrastAtPatch(patch,mean[i][j])
            local_probability[i][j] = computeLocalProbabiltyAtPatch(patch, mean[i][j])
            p25[i][j] = computep25AtPatch(patch)
            p75[i][j] = computep75AtPatch(patch)       
    return mean, median, variance, standard_deviation, skewness, kurtosis, mean_absolute_deviation, median__absolute_deviation, local_contrast, local_probability, p25, p75




#img = cv.imread("earth.jpg", 0)
img = cv.imread("nobita.png", 0)
print("=======original=======")
plt.imshow(img, cmap = "gray")
plt.show()

mean, median, variance, standard_deviation, skewness, kurtosis, mean_absolute_deviation, median__absolute_deviation, local_contrast, local_probability, p25, p75 = computeFOSF(img, 3, 3)
print("=======mean=======")
plt.imshow(mean, cmap = "gray")
plt.show()
print("=======median=======")
plt.imshow(median, cmap = "gray")
plt.show()
print("=======variance=======")
plt.imshow(variance, cmap = "gray")
plt.show()
print("=======standard deviation=======")
plt.imshow(standard_deviation, cmap = "gray")
plt.show()
print("=======skewness=======")
plt.imshow(skewness, cmap = "gray")
plt.show()
print("=======kurtosis=======")
plt.imshow(kurtosis, cmap = "gray")
plt.show()
print("=======mean absolute deviation=======")
plt.imshow(mean_absolute_deviation, cmap = "gray")
plt.show()
print("=======median absolute deviation=======")
plt.imshow(median__absolute_deviation, cmap = "gray")
plt.show()
print("=======local constrast=======")
plt.imshow(local_contrast, cmap = "gray")
plt.show()
print("=======local probability=======")
plt.imshow(local_probability, cmap = "gray")
plt.show()
print("=======P25=======")
plt.imshow(p25, cmap = "gray")
plt.show()
print("=======P75=======")
plt.imshow(p75, cmap = "gray")
plt.show()



plt.close()


