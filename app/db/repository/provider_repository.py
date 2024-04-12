from typing import Sequence

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from app.db.decorator import repository
from app.db.models.provider import Provider
from app.db.repository.respository_base import RepositoryBase


@repository(Provider)
class ProviderRepository(RepositoryBase):
    def __init__(self, session: Session):
        super().__init__(session=session)

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
        results = self.session.execute(stmt).scalars().all()
        return results

    def add_one(self, pseudonym: str, data_domain: str, provider_id: str) -> None:
        stmt = insert(Provider).values(
            pseudonym=pseudonym, data_domain=data_domain, provider_id=provider_id
        )
        self.session.execute(stmt)
        self.session.commit()
