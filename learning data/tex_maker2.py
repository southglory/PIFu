import cv2
import numpy as np

height= 512
width = 512
blank_image = np.zeros((height,width,3), np.uint8)
blank_image[:,:]=[200,200,200]#grey
grey_tex=np.array(blank_image,dtype=np.uint8)
print(grey_tex)
cv2.imshow('blue',grey_tex)
cv2.imwrite('data1/tex/_dif_05k_grey.jpg',grey_tex)