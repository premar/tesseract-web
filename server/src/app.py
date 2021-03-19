from flask import request, jsonify
from PIL import Image
import base64
import io
import pytesseract
import flask


app = flask.Flask(__name__)


@app.route('/v1/upload', methods=['POST'])
def upload():
    _json = request.json
    if _json and request.method == 'POST':
        image_base_64 = _json['image']
        image = base64.b64decode(image_base_64)
        buffer = io.BytesIO(image)
        image_buffer = Image.open(buffer)
        ocr_text = pytesseract.image_to_string(image_buffer)
        return ocr_text
    resp = jsonify("Bad Request")
    resp.status_code = 400
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
