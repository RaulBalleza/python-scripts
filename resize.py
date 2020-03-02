import cv2
import sys
import os

img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
width = int(sys.argv[3])
height = int(sys.argv[2])
dim = (width, height)

name = sys.argv[1].split("/")
name = name[-1]

#extension = name.split(".")
#extension = extension[-1]

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
path = os.getcwd() + "/resized_"+name
print("Saved on",path)
print('Resized Dimensions : ',resized.shape)
cv2.imwrite(path,resized)
#cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
