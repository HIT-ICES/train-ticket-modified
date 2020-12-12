#!/bin/zsh

echo 'framework test'

kubectl delete service --all -n default
kubectl delete deployment --all -n default
kubectl delete pods --all -n default


kubectl apply -f before.yaml
sleep 10s
kubectl apply -f after.yaml