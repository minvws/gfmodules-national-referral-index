from fastapi import Depends, Request
import inject
from app.authentication import resolve_authenticated_ura_number
from app.data import UraNumber
from app.db.db import Database
from app.config import Config, load_default_config
from app.services.referral_service import ReferralService
from app.services.pseudonym_service import PseudonymService

# TODO separate the FastAPI dependencies from the injector


def get_default_config() -> Config:
    return load_default_config()


def container_config(binder: inject.Binder) -> None:
    config = get_default_config()
    provider_id = config.app.provider_id

    db = Database(dsn=config.database.dsn, config=config)
    binder.bind(Database, db)

    referral_service = ReferralService(database=db)
    binder.bind(ReferralService, referral_service)

    pseudonym_service = PseudonymService(
        endpoint=config.pseudonym_api.endpoint,
        timeout=config.pseudonym_api.timeout,
        provider_id=provider_id,
        mtls_cert=config.pseudonym_api.mtls_cert,
        mtls_key=config.pseudonym_api.mtls_key,
        mtls_ca=config.pseudonym_api.mtls_ca,
    )
    binder.bind(PseudonymService, pseudonym_service)
    binder.bind(Config, config)


def get_database() -> Database:
    return inject.instance(Database)


def get_referral_service() -> ReferralService:
    return inject.instance(ReferralService)


def get_pseudonym_service() -> PseudonymService:
    return inject.instance(PseudonymService)


def authenticated_ura(
    request: Request, config: Config = Depends(get_default_config)
) -> UraNumber:
    """
    This is a dependency being used by FastAPI.
    """
    return resolve_authenticated_ura_number(request, config)


if not inject.is_configured():
    inject.configure(container_config)
