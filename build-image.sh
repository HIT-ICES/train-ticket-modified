#!/bin/bash


mvn clean package -Dmaven.test.skip=true

# delete docker image
echo 'delete docker image'
docker images | grep framework | awk '{print $1}' | xargs docker rmi
docker images | grep framework | awk '{print $3}' | xargs docker rmi
# build build image
echo ' build the image'
docker-compose -f docker-compose.yml -p framework build

echo 'tag the image'
docker images | grep framework | awk '{print "docker tag"" "$1":"$2 " ""172.31.22.168:5000/"$1":"$2}'| sh

echo 'docker push to the registry'
docker images | grep 172.31.22.168:5000/framework | awk '{print "docker push"" "$1":"$2}' | sh
