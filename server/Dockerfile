FROM ubuntu:latest
RUN apt-get install -y python3-pip python3-dev build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tesseract-ocr
COPY /src/ /app/
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]