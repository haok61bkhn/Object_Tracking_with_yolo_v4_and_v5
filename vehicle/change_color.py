import cv2
import numpy as np
img = cv2.imread("test.jpg")
img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = 255 - img
img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
print(img.shape)
cv2.imshow("aaf", img)
cv2.waitKey()
cv2.destroyAllWindows()