import cv2
import numpy as np

height= 10240
width = 10240
blank_image = np.zeros((height,width,3), np.uint8)
blank_image[:,:]=[230,230,0]#sky blue
blue_tex=np.array(blank_image,dtype=np.uint8)
print(blue_tex)
cv2.imshow('blue',blue_tex)
cv2.imwrite('data1/tex/_dif_10k_blue.jpg',blue_tex)