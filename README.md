"# flask-api-pose-estimation-YOLO-V8" 

# Useful Docker Commands
Unix
To delete all containers including its volumes use,
docker rm -vf $(docker ps -aq)

To delete all the images,
docker rmi -f $(docker images -aq)

Windows cmd.exe
for /F %i in ('docker images -a -q') do docker rmi -f %i

To delete all images
docker rmi $(docker images -a)

To delete containers which are in exited state
docker rm $(docker ps -a -f status=exited -q)

To delete containers which are in created state
docker rm $(docker ps -a -f status=created -q)

Build docker image from Dockerfile
docker build -t flask-api-pose-estimation-yolo-v8 .

Push image to dockerhub
docker push <your_username>/my-private-repo:tag
e.g., docker push moonbeam5115/flask-api-pose-estimation-yolo-v8:latest

The run command will spin up a new container for you to use.
The exec command will allow you to use a container that is already running.

add more information to repo