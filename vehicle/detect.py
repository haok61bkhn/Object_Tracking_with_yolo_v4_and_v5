from .tool.utils import *
from .tool.darknet2pytorch import Darknet
from .config import get_config
import cv2

class Detect_Vehicle:
    def __init__(self):
        opt=get_config()
        self.model=Darknet(opt.cfg)
        self.model.load_weights(opt.weights)
        self.model.to(opt.device)
        self.class_names=load_class_names(opt.names)
        self.size=(self.model.width,self.model.height)
        self.num_classes=80
    
    def detect(self,img,thresh=0.6):
        im0=img.copy()
        size=(img.shape[0],img.shape[1])
        img = cv2.resize(img, self.size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes=[]
        res=[]
        type_obj=[]
        score=[]
        for i in range(2):
            start = time.time()
            boxes = do_detect(self.model, img, thresh, self.num_classes, 0.4, 1)
            finish = time.time()
            if i == 1:
                print('%s: Predicted in %f seconds.' +str(finish - start))
        res_box=[]
        ims=[]
        for box in boxes:
          if(int(box[6])==2  or int(box[6])==3  or int(box[6])==5  or int(box[6])==7  ): # 2 3 5 7  is vehicle 
            x1 = int((box[0] - box[2] / 2.0) * size[1])
            y1 = int((box[1] - box[3] / 2.0) * size[0])
            x2 = int((box[0] + box[2] / 2.0) * size[1])
            y2 = int((box[1] + box[3] / 2.0) * size[0])
            imm=im0[y1:y2,x1:x2]

            if(imm.shape[0]>20 and imm.shape[1]>20):
             res_box.append([x1,y1,x2,y2])
             ims.append(imm)

    
        return res_box,ims

if __name__ == "__main__":
    X=Detector()
    img=cv2.imread("data_box/0.jpg")
    print(X.detect(img,0.3))
