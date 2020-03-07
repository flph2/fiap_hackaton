#!/bin/bash
case $1 in
    build)
	docker build -t fiap-hackaton .
    ;;
    clean)
	docker image prune
    ;;
esac
