import cv2

# Open the video
# cap = cv2.VideoCapture('../material/Video.mp4')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Store frames
frames = []
nf = 2
threshold = 50

for i in range(750):
    # Capture frame
    _, frame = cap.read()
    # Convert frame to grayscale
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # Append the greyscale frame
    frames.append(grey_frame)
    # Frame differencing
    if i >= nf:
        # Absolute difference between frames
        diff = cv2.absdiff(frames[i], frames[i - nf])
        # Thresholding
        _, mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
        cv2.imshow('Motion mask', mask)

    # Show frame
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
