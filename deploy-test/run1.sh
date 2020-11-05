#!/bin/bash
# to run the data-test
docker-compose -f zipkin.yml kill
docker ps -a | grep deploytest | awk '{print $1}' | xargs docker rm
docker-compose -f zipkin.yml build
docker-compose -f zipkin.yml up