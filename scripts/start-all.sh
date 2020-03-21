#!/bin/bash
docker-compose up --build -d
# Trick to avoid mysql DB connection fai
docker rm -f api
docker-compose up --build -d

