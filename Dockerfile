FROM moonbeam5115/flask-api-pose-estimation-yolo-v8:latest
WORKDIR /home/ubuntu/flask-api-pose-estimation-YOLO-V8
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git -y
RUN rm requirements.txt
RUN git init
RUN git pull https://github.com/moonbeam5115/flask-api-pose-estimation-YOLO-V8.git
RUN bash ./venv/bin/activate
RUN pip3 install --upgrade -r requirements.txt
EXPOSE 5000
