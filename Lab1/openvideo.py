import cv2

# Open the video path
# cap = cv2.VideoCapture("../material/Video.mp4")
cap = cv2.VideoCapture(0)

# Show the video
for i in range(10):
    # Capture frame by frame
    ret, frame = cap.read()

    # Write frame of the video
    cv2.imwrite(f"img{i}.jpg", frame)

    # Display video
    cv2.imshow('Frame', frame)
    cv2.waitKey(1)

# Release the allocated capture object
cap.release()
