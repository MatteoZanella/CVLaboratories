import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
background = None

# ===Alpha parameter===
alpha = 0.02

for _ in range(300):
    # Capture frame by frame
    _, frame = cap.read()
    # Color conversion
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    if background is None:
        background = gray_frame  # Set first frame as background
    else:
        # Background subtraction
        diff = cv2.absdiff(background, gray_frame)
        # Mask thresholding
        _, motion_mask = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
        # Background update
        cv2.addWeighted(gray_frame, alpha, background, 1 - alpha, 0, background)
        # Display
        cv2.imshow('Frame', frame)
        cv2.imshow('Motion mask', motion_mask)
        cv2.imshow('Background', background)
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
