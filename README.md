# tracking object
download model and video demo in https://drive.google.com/drive/folders/1YQXKm2FvZ_tNQOE-HELmSuz33oO3ocyj?usp=sharing

put model vehicle.weight at folder vehicle/weights

put model yolov5*.pt at folder yolov5/weights

- you can use your detection algorithm with:
  
  
  output detect must (input image):
    [[xmin1,ymin1,xmax1,ymax1],[xmin2,ymin2,xmax2,ymax2]....],imgs
    with imgs = [img1,img2...]
    img1 = image[ymin1:ymax1,xmin1:xmax1]
    ...
    
---------------------------------------------
or my detection algorithm
  that i proviced:
  
  
    1) yolov4 :
      you can modify config at vehicle/config.py
      and modify label object at line 34 vehicle/detect.py from label coco ( 0:person, 1 :car ....)
      
    2) yolov5:
      you can modify config at yolov5/config.py
      and modify label object at line 39 vehicle/detect.py from label coco ( 0:person, 1 :car ....)

run :
  put video demo and edit link video at file test.py

if you have any problem please contact me 
https://www.facebook.com/hoangquoc.hao
