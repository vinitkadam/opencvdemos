import numpy as np
import cv2
img = cv2.imread('home.jpg')
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img,None)
img=cv2.drawKeypoints(img,kp,img)
cv2.imwrite('sift_keypoints.jpg',img)