#!/bin/bash

docker rmi lei_python:3
docker build -t lei_python:3 .
docker tag lei_python:3 172.31.43.94:5000/lei_python:3
docker push 172.31.43.94:5000/lei_python:3