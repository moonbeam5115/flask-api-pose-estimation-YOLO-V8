FROM moonbeam5115/flask-api-pose-estimation-yolo-v8:latest
WORKDIR /home/ubuntu/flask-api-pose-estimation
RUN git pull https://github.com/moonbeam5115/flask-api-pose-estimation-YOLO-V8.git
RUN mv flask-api-pose-estimation-YOLO-V8/* .
RUN rm -rf flask-api-pose-estimation-YOLO-V8
RUN bash ./venv/bin/activate
RUN pip3 install --upgrade -r requirements.txt
CMD ['bash', 'run_app.sh']
