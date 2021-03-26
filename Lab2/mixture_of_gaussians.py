import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

lrnRate = -1
history = 200
nMixGauss = 200
bgRatio = 0.5
noiseSigma = 1

# backSub = cv2.bgsegm.createBackgroundSubtractorMOG(history, nMixGauss, bgRatio, noiseSigma)
backSub = cv2.createBackgroundSubtractorMOG2()

for _ in range(1000):
    # Open the video
    _, frame = cap.read()

    fgMask = backSub.apply(frame, lrnRate)
    bgMask = backSub.getBackgroundImage()

    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground mask', fgMask)
    cv2.imshow('Background mask', bgMask)
    cv2.waitKey(1)

del backSub
cap.release()
cv2.destroyAllWindows()
