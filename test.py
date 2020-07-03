from vehicle.detect import Detect_Vehicle
from yolov5.detect import Detector
import cv2
import numpy as np
from tracking import Sort



font= cv2.FONT_HERSHEY_SIMPLEX
# detector=Detect_Vehicle() # select yolov4
detector=Detector() # select yolov6
tracker = Sort(15, 3)
cap = cv2.VideoCapture("video.mp4")



while(cap.isOpened()):
    _,frame=cap.read()
    boxes,imgs = detector.detect(frame) # boxes : xmin,ymin,xmax,ymax
    boxes=np.array(boxes)
    if (len(boxes) != 0):
                    boxes = boxes.astype(int)
                    boxes = boxes + [-1,-1,1,1] 
                    trackers = tracker.update(boxes)
                    for idx, box in enumerate(trackers):
                        id = str(box[4])
                        box = [int(box[0]), int(box[1]), int(box[2]), int(box[3]), box[4]]
                        frame=cv2.rectangle(frame,(box[0],box[1]),(box[2],box[3]),(100,255,100),1)
                        frame = cv2.putText(frame,str(id),(box[0],box[1]),font,2,(0,200,100),2)
                        
        
    cv2.imshow("video",cv2.resize(frame,(500,500)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

