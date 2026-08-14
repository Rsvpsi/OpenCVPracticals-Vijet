import cv2

img=cv2.imread("images/sample.jpg")

rows,cols=img.shape[:2]

M=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)

rotate=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Rotated",rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()