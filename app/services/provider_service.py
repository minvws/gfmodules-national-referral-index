from typing import List

from app.data import Pseudonym, DataDomain, ProviderID
from app.db.db import Database
from app.db.models.providerentity import ProviderEntity
from app.db.repository.provider_repository import ProviderRepository
from app.response_models.providers import Provider


class ProviderService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def get_providers_by_domain_and_pseudonym(
        self, pseudonym: Pseudonym, data_domain: DataDomain
    ) -> List[Provider]:
        """
        Method that gets all the providers by pseudonym and data domain
        """
        with self.database.get_db_session() as session:
            provider_repository = session.get_repository(ProviderRepository)
            entities = provider_repository.find_many_providers(pseudonym, data_domain)

            return [self.hydrate_provider(entity) for entity in entities]

    def add_one_provider(
        self, pseudonym: Pseudonym, data_domain: DataDomain, provider_id: ProviderID
    ) -> None:
        with self.database.get_db_session() as session:
            provider_repository = session.get_repository(ProviderRepository)
            provider_repository.add_one(
                pseudonym=pseudonym, data_domain=data_domain, provider_id=provider_id
            )

    @staticmethod
    def hydrate_provider(entity: ProviderEntity) -> Provider:
        data_domain = DataDomain.from_str(entity.data_domain)
        if data_domain is None:
            raise ValueError("Invalid data domain")

        return Provider(
            provider_id=ProviderID(entity.provider_id),
            pseudonym=Pseudonym(entity.pseudonym),
            data_domain=data_domain,
        )
