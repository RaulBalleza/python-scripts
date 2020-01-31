import cv2
import sys
import os

img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
width = int(sys.argv[2])
height = int(sys.argv[3])
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
cv2.imwrite("resized_"+sys.argv[1],resized)
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
