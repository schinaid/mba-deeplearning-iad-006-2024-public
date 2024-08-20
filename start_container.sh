#! /bin/bash
docker build -t decision-tree-flask-app .

docker run -p 8000:8000 decision-tree-flask-app