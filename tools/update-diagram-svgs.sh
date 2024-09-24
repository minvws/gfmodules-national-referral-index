#!/bin/bash

set -e

SCRIPT=$(readlink -f $0)
BASEDIR=$(dirname $SCRIPT)/..

docker run \
  --rm \
  --user $UID:$GID \
  -v $BASEDIR/docs:/data/docs \
  plantuml/plantuml -tpng docs/puml

mv $BASEDIR/docs/puml/*.png $BASEDIR/docs/images
