#!/usr/bin/env bash

set -e

SECRETS_DIR=secrets

echo "Downloading generated certs from secrets container"

response=$(curl --write-out '%{http_code}' --output /dev/null http://secrets/README.md)

if [[ "$response" -ne 200 ]] ; then
  echo "Unable to download secrets from secrets container"
  echo "Did you start the docker compose project from the coordination repo?"
  exit 1
fi

curl -f http://secrets/localization/localization.crt -o $SECRETS_DIR/localization.crt
curl -f http://secrets/localization/localization.key -o $SECRETS_DIR/localization.key
curl -f http://secrets/uzi-server-ca.crt -o $SECRETS_DIR/uzi-server-ca.crt

echo "Downloaded generated certs from secrets container"
