import cv2
image = cv2.imread(input("Enter Full Path Of File: "))
resixe=cv2.resize(image,(400,600))
gray_image = cv2.cvtColor(resixe, cv2.COLOR_BGR2GRAY)
inverted_image = 250 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 250 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=250.0)
cv2.imshow("Original Image", resixe)
cv2.imshow("Pencil Sketch of User Photo", pencil_sketch)
cv2.waitKey(0)