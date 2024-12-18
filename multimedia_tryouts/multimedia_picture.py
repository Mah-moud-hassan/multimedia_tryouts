# import cv2 
# path = 'black_clover.jpeg'
# img = cv2.imread(path , cv2.IMREAD_COLOR)
# cv2.imshow('asta' , img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#################################################

# import cv2 
# path = 'black_clover.jpeg'
# img = cv2.imread(path , cv2.IMREAD_GRAYSCALE)
# cv2.imshow('asta' , img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################

# import cv2 
# path = 'black_clover.jpeg'
# img = cv2.imread(path , cv2.IMREAD_COLOR)
# cv2.imshow('asta' , img)
# print(img.shape)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################

# import cv2 
# import numpy as np
# from numpy import shape
# path = 'black_clover.jpeg'
# img = cv2.imread(path , cv2.IMREAD_COLOR)
# print('first pixel of color image:' , 
#       cv2.imread(path , cv2.IMREAD_COLOR)[0,0,:])
# print('first pixel of graycastle image:' , 
#       cv2.imread(path , cv2.IMREAD_GRAYSCALE)[0,0])    
# cv2.imshow('asta' , img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

###################################################

# import cv2 
# from matplotlib import pyplot as plt 
# img = cv2.imread('black_clover.jpeg')
# b,g,r=cv2.split(img)
# img= cv2.merge([r,g,b])
# cv2.putText(img , 'asta' , (10 , 300) , 0,3 , (255,0,0) ,5)
# plt.imshow(img)
# plt.show()
