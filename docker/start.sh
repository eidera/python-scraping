#! /bin/sh

NETWORK_NAME="scraping_default"

echo "docker build -t scraping-base -f ./build/Dockerfile ." 1>&2
docker build -t scraping-base -f ./build/Dockerfile .

echo "docker network create --driver bridge ${NETWORK_NAME}" 1>&2
docker network create --driver bridge ${NETWORK_NAME}

echo "docker-compose up -d" 1>&2
docker-compose up -d
