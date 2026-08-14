import cv2

img = cv2.imread("images/sample.jpg")

cv2.line(img,(20,20),(300,20),(255,0,0),3)

cv2.rectangle(img,(50,50),(250,180),(0,255,0),3)

cv2.circle(img,(350,150),60,(0,0,255),3)

cv2.putText(img,"OpenCV",(100,350),
cv2.FONT_HERSHEY_SIMPLEX,
1,(255,255,255),2)

cv2.imshow("Shapes",img)

cv2.waitKey(0)
cv2.destroyAllWindows()