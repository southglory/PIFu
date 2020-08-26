import cv2
import numpy as np

dif=cv2.imread('data1/tex/rp_dennis_posed_004_dif_2k.jpg',cv2.IMREAD_COLOR)
pixlist = dif.tolist()
print(dif.shape)#(y length, x length, channels)
for i in range(0,2048):
    for j in range(0,2048):
        pixlist[i][j]=[0,230,230]
yellow=np.array(pixlist,dtype=np.uint8)
print(yellow)
cv2.imshow('yellow',yellow)
cv2.imwrite('data1/tex/rp_dennis_posed_004_dif_2k_yellow.jpg',yellow)