#!/bin/bash
# to run the data-test
docker-compose -f docker-compose-changeverifycode.yml -p changevertest kill
docker ps -a | grep changevertest | awk '{print $1}' | xargs docker rm -f
docker images | grep changevertest | awk '{print $3}' | xargs docker rmi -f
docker-compose -f docker-compose-changeverifycode.yml -p changevertest build
docker-compose -f docker-compose-changeverifycode.yml -p changevertest up