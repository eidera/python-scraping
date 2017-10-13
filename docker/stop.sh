#! /bin/sh

NETWORK_NAME="scraping_default"

echo "docker-compose down" 1>&2
docker-compose down

echo "docker network rm ${NETWORK_NAME}" 1>&2
docker network rm ${NETWORK_NAME}
