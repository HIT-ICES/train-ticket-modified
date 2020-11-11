#!/bin/zsh


mvn clean package -Dmaven.test.skip=true

# delete docker image
echo 'delete docker image'
docker images | grep leizipkin | awk '{print $1}' | xargs docker rmi

# build build image
echo ' build the image'
docker-compose -f docker-compose.yml -p leizipkin build

# tag image
echo 'tag the image'
docker images | grep leizipkin | awk '{print "docker tag"" "$1":"$2 " ""192.168.1.104:5000/"$1":"$2}'| sh

# docker push
echo 'docker push to the registry'
docker images | grep 192.168.1.104:5000/leizipkin | awk '{print "docker push"" "$1":"$2}' | sh