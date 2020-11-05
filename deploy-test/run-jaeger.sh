#!/bin/bash

docker-compose -f user-compose-withjager.yml kill
docker ps -a | grep jaegertest | awk '{print $1}' | xargs docker rm -f
docker-compose -f user-compose-withjager.yml -p jaegertest build
docker-compose -f user-compose-withjager.yml -p jaegertest up