import cv2
import numpy as np

"""img = cv2.imread('C:/Coding/Python Scripts/computahviseon/download.png',1)
cv2.imshow("Orig",img)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
low = np.array([150,150,25])
up = np.array([255,255,255])
masked = cv2.inRange(hsv,low,up);
cv2.imshow("Masked",masked)"""

vid = cv2.VideoCapture("C:/Coding/Python Scripts/computahviseon/gates.mp4")
if(vid.isOpened() == False):
    print("Error opening video")
while(vid.isOpened()):
    ret,frm = vid.read()
    if(ret):
        #cv2.imshow("Original",frm)
        orig = frm
        frm = cv2.cvtColor(frm,cv2.COLOR_BGR2HSV)
        #cv2.imshow("HSV",frm)

        low = np.array([15,65,20])
        up = np.array([105,230,112])


        frm = cv2.inRange(frm,low,up)
        frm = cv2.GaussianBlur(frm,(5,5),cv2.BORDER_ISOLATED)

        contours,_ = cv2.findContours(frm,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        minRect = [None]*len(contours)
        minEllipse = [None]*len(contours)
        for i, c in enumerate(contours):
            minRect[i] = cv2.minAreaRect(c)
            if c.shape[0] > 5:
                minEllipse[i] = cv2.fitEllipse(c)

        for i, contour in enumerate(contours):
            approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour,True),True)

            #cv2.drawContours(orig,[approx],-1,(0,0,255),5)
            x,y,w,h =  cv2.boundingRect(frm)
            orig = cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)
            #if c.shape[0] > 5:
            #    cv2.ellipse(orig, minEllipse[i], (0,255,0), 2)

            box = cv2.boxPoints(minRect[i])
            box = np.intp(box) #np.intp: Integer used for indexing (same as C ssize_t; normally either int32 or int64)
            cv2.drawContours(orig, [box], 0, (0,255,0),2)
        cv2.imshow("Processed",orig)
        
        ki = cv2.waitKey(17)
        if(ki==113):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()