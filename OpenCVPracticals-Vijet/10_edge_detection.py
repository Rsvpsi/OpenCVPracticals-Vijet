import cv2

img=cv2.imread("images/sample.jpg",0)

edge=cv2.Canny(img,100,200)

cv2.imshow("Edges",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()