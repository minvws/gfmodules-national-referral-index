from typing import Sequence

from sqlalchemy import select, insert

from app.data import ProviderID, DataDomain, Pseudonym
from app.db.decorator import repository
from app.db.models.providerentity import ProviderEntity
from app.db.repository.respository_base import RepositoryBase


@repository(ProviderEntity)
class ProviderRepository(RepositoryBase):
    def find_many_providers(
        self, pseudonym: Pseudonym, data_domain: DataDomain
    ) -> Sequence[ProviderEntity]:
        """
        find many providers with pseudonym and data domain
        """
        stmt = (
            select(ProviderEntity)
            .where(ProviderEntity.pseudonym == str(pseudonym))
            .where(ProviderEntity.data_domain == str(data_domain))
        )
        return self.db_session.execute(stmt).scalars().all()    # type: ignore

    def add_one(self, pseudonym: Pseudonym, data_domain: DataDomain, provider_id: ProviderID) -> None:
        stmt = insert(ProviderEntity).values(
            pseudonym=str(pseudonym), data_domain=str(data_domain), provider_id=str(provider_id)
        )
        self.db_session.execute(stmt)
        self.db_session.commit()
