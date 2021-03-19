# tesseract-web

Docker image with python flask serving as API and tesseract-ocr software. Simply send an image and tesseract will return the text inside the image.

### Getting Started

Build the server image:

```
sudo docker build -t tesseract-web .
```

Start the image with:
```
sudo docker run -p 127.0.0.1:5000:5000 tesseract-web
```

### Usage

Send a POST request with the image as json parameter. See the example inside the client.