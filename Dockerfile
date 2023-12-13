# Use the Ubuntu 22.04 as the base image
FROM ubuntu:22.04
RUN apt update && apt install -y python3 python3-venv python3-pip

WORKDIR /DDSI_SEM2/
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DB_USERNAME = "X8904938"
ENV DB_PASSWORD = "X8904938"
CMD ["flask","run"]

