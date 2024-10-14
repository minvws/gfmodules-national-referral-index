import abc
import textwrap

from app.data import UraNumber
from fastapi import HTTPException
from starlette.requests import Request
from uzireader.uziserver import UziServer


class URANumberFinder(abc.ABC):
    @abc.abstractmethod
    def find(self) -> UraNumber:
        ...


class ConfigOverridenURANumberFinder(URANumberFinder):
    _config_value: str

    def __init__(self, config_value: str) -> None:
        self._config_value = config_value

    def find(self):
        return UraNumber(self._config_value)


class StarletteRequestURANumberFinder(URANumberFinder):
    _CERT_START = "-----BEGIN CERTIFICATE-----"
    _CERT_END = "-----END CERTIFICATE-----"

    _cert: str

    def __init__(self, request: Request) -> None:
        if "x-proxy-ssl_client_cert" not in request.headers:
            raise HTTPException(
                status_code=401,
                detail="Missing client certificate",
            )
        self._cert = request.headers["x-proxy-ssl_client_cert"]

    def _enforce_cert_newlines(self, cert_data: str) -> str:
        cert_data = (
            cert_data.split(self._CERT_START)[-1].split(self._CERT_END)[0].strip()
        )
        result = self._CERT_START
        result += "\n"
        result += "\n".join(textwrap.wrap(cert_data.replace(" ", ""), 64))
        result += "\n"
        result += self._CERT_END

        return result

    def find(self) -> UraNumber:
        formatted_cert = self._enforce_cert_newlines(self._cert)
        uzi_server = UziServer(verify="SUCCESS", cert=formatted_cert)

        return UraNumber(uzi_server["SubscriberNumber"])
