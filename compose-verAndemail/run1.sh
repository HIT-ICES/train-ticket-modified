#!/bin/bash
# to run the data-test
docker-compose -f docker-compose-testThestationinfo.yml -p traveltest kill
docker ps -a | grep traveltest | awk '{print $1}' | xargs docker rm -f
docker images | grep traveltest | awk '{print $3}' | xargs docker rmi -f
docker-compose -f docker-compose-testThestationinfo.yml -p traveltest build
docker-compose -f docker-compose-testThestationinfo.yml -p traveltest up