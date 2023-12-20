import os, cv2

img = cv2.imread(os.path.join('.','whiteboard.jpeg'))

img = cv2.resize(img,(1000,500))
print(img.shape)

#line
cv2.line(img,(100,150),(200,300),(0,255,0),3)

#rectangle
cv2.rectangle(img,(350,50),(950,450),(0,0,255),5)

#circle
cv2.circle(img,(500,250),100,(255,0,0),5)

#text
cv2.putText(img,'Hello World',(600,300),cv2.FONT_HERSHEY_SIMPLEX,2,(125,225,5),5)

cv2.imshow('image', img)
cv2.waitKey(0)