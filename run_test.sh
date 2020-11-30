#!/bin/bash
# to run the data-test

mvn clean package -Dmaven.test.skip=true

docker-compose -f docker-compose.yml -p alltest kill
docker ps -a | grep alltest | awk '{print $1}' | xargs docker rm -f
docker images | grep alltest | awk '{print $3}' | xargs docker rmi -f
docker-compose -f docker-compose.yml -p alltest build
docker-compose -f docker-compose.yml -p alltest up

sleep 10s

echo 'initDataPrice'
curl --request GET -sL \
     --url 'http://localhost:18000/initDataPrice'

sleep 5s
echo 'initDataTravel'
curl --request GET -sL \
     --url 'http://localhost:18000/initDataTravel'

sleep 5s
echo 'initDataUser'
curl --request GET -sL \
     --url 'http://localhost:18000/initDataUser'