#!/bin/bash
# to run the data-test
docker-compose -f docker-compose.yml -p alltest kill
docker ps -a | grep alltest | awk '{print $1}' | xargs docker rm -f
docker images | grep alltest | awk '{print $3}' | xargs docker rmi -f
docker-compose -f docker-compose.yml -p alltest build
docker-compose -f docker-compose.yml -p alltest up


curl --request GET -sL \
     --url 'http://localhost:18000/initDataPrice'

curl --request GET -sL \
     --url 'http://localhost:18000/initDataTravel'

curl --request GET -sL \
     --url 'http://localhost:18000/initDataUser'