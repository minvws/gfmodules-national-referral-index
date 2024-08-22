import textwrap

from fastapi import HTTPException
from starlette.requests import Request
from uzireader.uziserver import UziServer

from app.data import UraNumber


def authenticated_ura(request: Request) -> UraNumber:
    cert = request.headers["x-proxy-ssl_client_cert"]
    if not cert:
        raise HTTPException(status_code=401)

    formatted_cert = enforce_cert_newlines(cert)
    uzi_server = UziServer(verify="SUCCESS", cert=formatted_cert)
    return UraNumber(uzi_server["SubscriberNumber"])


def enforce_cert_newlines(cert_data: str) -> str:
    cert_data = (
        cert_data.split("-----BEGIN CERTIFICATE-----")[-1]
        .split("-----END CERTIFICATE-----")[0]
        .strip()
    )
    return (
        "-----BEGIN CERTIFICATE-----\n"
        + "\n".join(textwrap.wrap(cert_data.replace(" ", ""), 64))
        + "\n-----END CERTIFICATE-----"
    )
