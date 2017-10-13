#! /bin/sh

ENV_LANG="LANG=ja_JP.UTF-8"
PYTHON="/root/.pyenv/shims/python -B"
SCRIPT="run.py"
COMMAND="${PYTHON} ${SCRIPT}"

echo "docker run --rm -e ${ENV_LANG} -v `pwd`:/app --net scraping_default --link scraping-db:scraping-db scraping-base ${COMMAND}" 1>&2
docker run --rm -e ${ENV_LANG} -v `pwd`:/app --net scraping_default --link scraping-db:scraping-db scraping-base ${COMMAND}
