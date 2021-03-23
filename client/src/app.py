import base64
import io
import numpy as np
import requests
import pyscreenshot as grab
from cv2 import cv2


def create_opencv_image_from_stringio(img_stream, cv2_img_flag=0):
    img_stream.seek(0)
    img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)


ENDPOINT = "http://127.0.0.1:5000/v1/upload"


input_buffer = io.BytesIO()
py_image = grab.grab()
py_image.save(input_buffer, format='JPEG')
py_image.close()

cv_image = create_opencv_image_from_stringio(input_buffer)
cv_image_grey = cv2.threshold(cv_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv_image_grey = cv2.medianBlur(cv_image_grey, 3)
output_buffer = cv2.imencode('.jpg', cv_image_grey)[1].tobytes()

image_base_64 = base64.b64encode(output_buffer)
response = requests.post(ENDPOINT, json={"image": image_base_64.decode('utf-8')})

print(response.text)
