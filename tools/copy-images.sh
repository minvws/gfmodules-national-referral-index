#!/bin/bash

set -ex

SCRIPT=$(readlink -f $0)
BASEDIR=$(dirname $SCRIPT)/..

cd $BASEDIR
cp ../gfmodules-coordination-private/docs/images/structurizr-LocalizeInterface.svg docs/images/structurizr-LocalizeInterface.svg
cp ../gfmodules-coordination-private/docs/images/structurizr-UpdateLocalizationDataInterface.svg docs/images/structurizr-UpdateLocalizationDataInterface.svg
