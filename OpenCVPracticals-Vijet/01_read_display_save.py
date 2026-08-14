import cv2

img = cv2.imread("images/sample.jpg")

cv2.imshow("Original Image", img)

cv2.imwrite("output/saved_image.jpg", img)

cv2.waitKey(0)

cv2.destroyAllWindows()