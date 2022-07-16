import cv2
import numpy as np



vid = cv2.VideoCapture("gates.mp4") #Read the video frame by frame

#If any error is found in reading the video then let the user know
if(vid.isOpened() == False):
    print("Error opening video")

#While new frame available, process the frame and mark out the gates
while(vid.isOpened()):
    ret,frm = vid.read()
    
    if(ret):
        orig = frm
        frm = cv2.cvtColor(frm,cv2.COLOR_BGR2HSV) # Convert to HSV image 

        low = np.array([15,65,20])
        up = np.array([105,230,112])


        frm = cv2.inRange(frm,low,up)
        # Get a binary image by thresholding the HSV image within a range of HSV values 
        # and blur it to get smoother edges
        frm = cv2.GaussianBlur(frm,(5,5),cv2.BORDER_ISOLATED)

        contours,_ = cv2.findContours(frm,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # Detect the contours 

        # Create a list 
        minRect = [None]*len(contours)

        #Find the minimum area bounding rectangle for every contour detected
        for i, c in enumerate(contours):
            minRect[i] = cv2.minAreaRect(c)

        # Draw an approximated polygon for the contours detected
        for i, contour in enumerate(contours):
            approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour,True),True)
            # Get the bounding rectangle of the entire gate
            x,y,w,h =  cv2.boundingRect(frm)
            orig = cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)

            box = cv2.boxPoints(minRect[i])
            box = np.intp(box) 
            #Draw the boxes
            cv2.drawContours(orig, [box], 0, (0,255,0),2)

            #Show the final image
        cv2.imshow("Processed",orig)
        
        ki = cv2.waitKey(17) #To play at the correct framerate
        if(ki==113):
            break
    else:
        break

vid.release()
#Release videocapture after done and destroy all windows after which the python program exits.
cv2.destroyAllWindows()