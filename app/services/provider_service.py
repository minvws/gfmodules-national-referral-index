from typing import Sequence, cast

from app.db.models.provider import Provider
from app.db.db import Database
from app.db.repository.provider_repository import ProviderRepository
from app.db.session import DbSession


class ProviderService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def get_providers_by_domain_and_pseudonym(
        self, pseudonym: str, data_domain: str
    ) -> Sequence[Provider]:
        """
        Method that gets all the providers by pseudonym and data domain
        """
        with self.database.get_db_session() as session:
            provider_repository = self.get_provider_repository(session)

            results = provider_repository.find_many_providers(pseudonym, data_domain)
            return results

    def add_one_provider(
        self, pseudonym: str, data_domain: str, provider_id: str
    ) -> None:
        with self.database.get_db_session() as session:
            provider_repository = self.get_provider_repository(session)
            provider_repository.add_one(
                pseudonym=pseudonym, data_domain=data_domain, provider_id=provider_id
            )

    @staticmethod
    def get_provider_repository(session: DbSession) -> ProviderRepository:
        """
        private method to get repository for providers
        """
        return cast(
            ProviderRepository,
            session.get_repository(Provider)
        )
