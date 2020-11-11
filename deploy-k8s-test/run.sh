#!/bin/zsh

kubectl delete service --all
kubectl delete deployment --all
kubectl delete pods --all

kubectl apply -f zipkin.yaml
kubectl apply -f ts-deploy-before.yaml

echo 'sleep 1 minute'
sleep 1m

echo 'deploy the service'
kubectl apply -f ts-deploy-after.yaml