# Test basique d'open csv show + resize de l'image + écriture.


import numpy as np
from matplotlib import pyplot as plt
import cv2

a = 1000.

img = cv2.imread(r"C:\Users\dupont\Pictures\moto.jpg",cv2.IMREAD_COLOR )
height, width, depth = img.shape
imgScale = a/width
newX,newY = img.shape[1]*imgScale, img.shape[0]*imgScale
nimg = cv2.resize(img,(int(newX),int(newY)))
cv2.imshow("Afficher avec CV2",nimg)
cv2.waitKey(0)
cv2.imwrite("MOTOrécrite.jpg",nimg)
cv2.destroyAllWindows()
