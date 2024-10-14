import inject
from app.db.db import Database
from app.config import Config
from app.dependencies import get_default_config
from app.services.referral_service import ReferralService
from app.services.pseudonym_service import PseudonymService


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


def configure() -> None:
    inject.configure(container_config, once=True)
