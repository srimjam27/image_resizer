import cv2

source = "simp.jpg"
dest = "std_attendance.jpg"
sc = int(input("ENTER THE SCALE BTW 1 to 100 TO WHICH U WANT TO RESIZE THE IMAGE "))
scale = sc / 100
img = cv2.imread(source)

new_width = int(img.shape[1] * scale)
new_height = int(img.shape[0] * scale)

dsize = (new_width, new_height)

output = cv2.resize(img, dsize)

cv2.imwrite(dest, output)
cv2.waitKey(0)
