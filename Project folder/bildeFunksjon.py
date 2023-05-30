import cv2
import os

bilde_mappe = "mappe "

bilde = cv2.VideoCapture(0)

bilde.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
bilde.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

ret, frame = bilde.read()

frame = cv2.rotate(frame, cv2.ROTATE_180)

bilde_sted = os.path.join(bilde_mappe, 'image.jgp')

cv2.imwrite(bilde_sted, frame)

bilde.release()