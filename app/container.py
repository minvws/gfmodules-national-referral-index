
import inject
from db.db import Database
from config import get_config
from app.services.provider_service import ProviderService


def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    provider_service = ProviderService(
        database=db
    )
    binder.bind(ProviderService, provider_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_provider_service() -> ProviderService:
    return inject.instance(ProviderService)


if not inject.is_configured():
    inject.configure(container_config)
