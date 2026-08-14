import cv2

img=cv2.imread("images/sample.jpg")

gaussian=cv2.GaussianBlur(img,(9,9),0)

median=cv2.medianBlur(img,9)

cv2.imshow("Gaussian",gaussian)
cv2.imshow("Median",median)

cv2.waitKey(0)
cv2.destroyAllWindows()