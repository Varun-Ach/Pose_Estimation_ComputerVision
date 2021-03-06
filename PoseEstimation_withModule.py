import cv2
import time
import PoseEstimationModule as pm

cap = cv2.VideoCapture('videos/3.mp4')
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 10, (0, 0, 255), cv2.FILLED) # Tracking right elbow
        print(lmList)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)