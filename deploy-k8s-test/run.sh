#!/bin/zsh

kubectl delete service --all
kubectl delete deployment --all
kubectl delete pods --all

kubectl apply -f zipkin.yaml
kubectl apply -f ts-deploy-before.yaml
kubectl apply -f ts-deploy-after.yaml