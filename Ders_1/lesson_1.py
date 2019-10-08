import cv2
import numpy as np

image = cv2.imread("seinfeldcast.jpg",0) 
image2 = cv2.imread("newseinfeld.jpg")
print(type(image))
cv2.imshow("seinfeld image",image)
cv2.imshow("seinfeldcast",image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("newseinfeld.jpg",image)



#deneme

