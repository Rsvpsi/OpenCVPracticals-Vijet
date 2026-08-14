import cv2
import numpy as np

img=cv2.imread("images/sample.jpg",0)

kernel=np.ones((5,5),np.uint8)

tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("TopHat",tophat)
cv2.imshow("BlackHat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()