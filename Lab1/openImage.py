import cv2

# Open image
image = cv2.imread("../material/Google.jpg", 1)

# Show image
cv2.imshow('Hello world', image)
cv2.waitKey(0)
