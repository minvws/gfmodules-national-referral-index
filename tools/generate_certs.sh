#!/usr/bin/env bash

set -e

SECRETS_DIR=secrets

create_key_pair () {
  echo "generating keypair and certificate $2/$3 with CN:$4"
  mkdir -p `dirname "$2/$3.crt"`
  openssl genrsa -out $2/$3.key 2048
  openssl rsa -in $2/$3.key -pubout > $2/$3.pub
  openssl req -new -sha256 \
    -key $2/$3.key \
    -subj "/C=NL/L=Den Haag/O=MinVWS/OU=RDO/CN=$4" \
    -out $2/$3.csr
  openssl x509 -req -days 500 -sha256 \
    -in $2/$3.csr \
    -CA $1.crt \
    -CAkey $1.key \
    -CAcreateserial \
    -out $2/$3.crt
  rm $2/$3.csr
}

###
# Create ca for ssl selfsigned certificates
###
if [[ ! -f $SECRETS_DIR/ssl_cacert.crt ]]; then
  openssl genrsa -out $SECRETS_DIR/ssl_cacert.key 4096
  openssl req -x509 -new -nodes -sha256 -days 1024 \
	  -key $SECRETS_DIR/ssl_cacert.key \
	  -out $SECRETS_DIR/ssl_cacert.crt \
	  -subj "/C=NL/L=Den Haag/O=MinVWS/OU=RDO/CN=server-test-ca"
fi

###
# Create ca for client selfsigned certificates
###
if [[ ! -f $SECRETS_DIR/clients_cacert.crt ]]; then
  openssl genrsa -out $SECRETS_DIR/clients_cacert.key 4096
  openssl req -x509 -new -nodes -sha256 -days 1024 \
	  -key $SECRETS_DIR/clients_cacert.key \
	  -out $SECRETS_DIR/clients_cacert.crt \
	  -subj "/C=NL/L=Den Haag/O=MinVWS/OU=RDO/CN=clients-test-ca"
fi

###
# SSL certs
###
if [[ ! -f $SECRETS_DIR/ssl/server.crt ]]; then
  create_key_pair $SECRETS_DIR/ssl_cacert $SECRETS_DIR/ssl "server" "zmodules.localisation-service.pgo"
fi

###
# client certs
###
if [[ ! -f $SECRETS_DIR/client/client.crt ]]; then
  echo "generating keypair and certificate $SECRETS_DIR/client/client"
  mkdir -p `dirname "$SECRETS_DIR/client/client.crt"`
  openssl genrsa -out $SECRETS_DIR/client/client.key 2048
  openssl rsa -in $SECRETS_DIR/client/client.key -pubout > $SECRETS_DIR/client/client.pub
  openssl req -new -sha256 \
    -key $SECRETS_DIR/client/client.key \
    -subj "/C=NL/L=Den Haag/O=MinVWS/OU=RDO/CN=client/serialNumber=1234ABCD" \
    -addext "subjectAltName = otherName:2.5.5.5;IA5STRING:2.16.528.1.1003.1.3.5.5.2-1-12345678-S-90000123-00.000-00000000" \
    -out $SECRETS_DIR/client/client.csr
  openssl x509 -req -days 500 -sha256 \
    -in $SECRETS_DIR/client/client.csr \
    -CA $SECRETS_DIR/clients_cacert.crt \
    -CAkey $SECRETS_DIR/clients_cacert.key \
    -CAcreateserial \
    -copy_extensions copyall \
    -out $SECRETS_DIR/client/client.crt
  rm $SECRETS_DIR/client/client.csr
fi
