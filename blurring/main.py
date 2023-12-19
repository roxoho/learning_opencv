import cv2, os

img= cv2.imread(os.path.join('.', 'test.jpg'))


resized_img=cv2.resize(img,(660,340))

k_size=7

img_blur=cv2.blur(resized_img,(k_size,k_size))

gauss_blur = cv2.GaussianBlur(resized_img,(k_size,k_size),3)

median_blur = cv2.medianBlur(resized_img,k_size)



cv2.imshow('image',resized_img)
cv2.imshow('image_blur',img_blur)
cv2.imshow('gauss_blur',gauss_blur)
cv2.imshow('median_blur',median_blur)
cv2.waitKey(0)


