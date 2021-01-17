#!/bin/zsh


mvn clean package -Dmaven.test.skip=true

# delete docker image
echo 'delete docker image'
docker images | grep nocirclesmell | awk '{print $1}' | xargs docker rmi -f
docker images | grep nocirclesmell | awk '{print $3}' | xargs docker rmi -f
# build build image
echo ' build the image'
docker-compose -f docker-compose.yml -p nocirclesmell build

echo 'tag the image'
docker images | grep nocirclesmell | awk '{print "docker tag"" "$1":"$2 " ""192.168.1.104:5000/"$1":"$2}'| sh

echo 'docker push to the registry'
docker images | grep 192.168.1.104:5000/nocirclesmell | awk '{print "docker push"" "$1":"$2}' | sh
