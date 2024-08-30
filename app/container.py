
import inject
from app.db.db import Database
from app.config import get_config
from app.services.provider_service import ProviderService
from app.services.pseudonym_service import PseudonymService


def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    provider_service = ProviderService(
        database=db
    )
    binder.bind(ProviderService, provider_service)

    pseudonym_service = PseudonymService(
        endpoint=config.pseudonym_api.endpoint,
        timeout=config.pseudonym_api.timeout,
        mtls_cert=config.pseudonym_api.mtls_cert,
        mtls_key=config.pseudonym_api.mtls_key,
        mtls_ca=config.pseudonym_api.mtls_ca,
    )
    binder.bind(PseudonymService, pseudonym_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_provider_service() -> ProviderService:
    return inject.instance(ProviderService)


def get_pseudonym_service() -> PseudonymService:
    return inject.instance(PseudonymService)


if not inject.is_configured():
    inject.configure(container_config)
