#!/bin/bash

export DB_HOST=127.0.0.1
export DB_PASS=Password123!

docker run \
  -p 127.0.0.1:3306:3306 \
  --name myappdb \
  --rm \
  -v /home/antoine/docs/purpleweb/exercices/db/init.sql:/docker-entrypoint-initdb.d/1.sql \
  -e MARIADB_ROOT_PASSWORD=$DB_PASS \
  -d \
  mariadb:latest

flask --debug run