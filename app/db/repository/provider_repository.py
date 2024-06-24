from typing import Sequence

from sqlalchemy import select, insert

from app.db.decorator import repository
from app.db.models.provider import Provider
from app.db.repository.respository_base import RepositoryBase


@repository(Provider)
class ProviderRepository(RepositoryBase):
    def find_many_providers(
        self, pseudonym: str, data_domain: str
    ) -> Sequence[Provider]:
        """
        find many providers with pseudonym and data domain
        """
        stmt = (
            select(Provider)
            .where(Provider.pseudonym == pseudonym)
            .where(Provider.data_domain == data_domain)
        )
        return self.db_session.execute(stmt).scalars().all()    # type: ignore

    def add_one(self, pseudonym: str, data_domain: str, provider_id: str) -> None:
        stmt = insert(Provider).values(
            pseudonym=pseudonym, data_domain=data_domain, provider_id=provider_id
        )
        self.db_session.execute(stmt)
        self.db_session.commit()
