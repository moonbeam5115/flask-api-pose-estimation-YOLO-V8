FROM moonbeam5115/flask-api-pose-estimation-yolo-v8:latest
WORKDIR /home/ubuntu/flask-api-pose-estimation-YOLO-V8
COPY . .
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip python3-venv \
    ffmpeg libsm6 libxext6 git -y
RUN python3 -m venv ./venv
RUN bash ./venv/bin/activate
RUN pip3 install --upgrade -r requirements.txt
EXPOSE 5000
CMD ["bash", "run run_app.sh"]
