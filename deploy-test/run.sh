#!/bin/bash
# to run the data-test
docker-compose -f user-compose.yml kill
docker ps -a | grep datatest | awk '{print $1}' | xargs docker rm
docker-compose -f user-compose.yml -p datatest build
docker-compose -f user-compose.yml -p datatest up