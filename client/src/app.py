import base64
import io
import requests
import pyscreenshot as grab

ENDPOINT = "http://127.0.0.1:5000/v1/upload"

buffer = io.BytesIO()
image = grab.grab()
image.save(buffer, format='PNG')
image.close()
image_base_64 = base64.b64encode(buffer.getvalue())
response = requests.post(ENDPOINT, json={"image": image_base_64.decode('utf-8')})
print(response.text)
