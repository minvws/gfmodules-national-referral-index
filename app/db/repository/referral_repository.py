from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.data import UraNumber, DataDomain, Pseudonym
from app.db.decorator import repository
from app.db.models.referral import ReferralEntity
from app.db.repository.respository_base import RepositoryBase


@repository(ReferralEntity)
class ReferralRepository(RepositoryBase):
    def find_one(
        self, pseudonym: Pseudonym, data_domain: DataDomain, ura_number: UraNumber
    ) -> ReferralEntity:
        try:
            stmt = select(ReferralEntity).where(
                ReferralEntity.ura_number == str(ura_number),
                ReferralEntity.data_domain == str(data_domain),
                ReferralEntity.pseudonym == str(pseudonym),
            )
            result: ReferralEntity = self.db_session.execute(stmt).scalars().first()
            return result
        except (SQLAlchemyError, TypeError, ValueError) as exc:
            raise exc

    def query_referrals(self,
        pseudonym: Pseudonym | None, data_domain: DataDomain | None, ura_number: UraNumber | None
        ) -> Sequence[ReferralEntity]:
        try:
            stmt = select(ReferralEntity)

            if ura_number is not None:
                stmt = stmt.where(ReferralEntity.ura_number == str(ura_number))

            if pseudonym is not None:
                stmt = stmt.where(ReferralEntity.pseudonym == str(pseudonym))

            if data_domain is not None:
                stmt = stmt.where(ReferralEntity.data_domain == str(data_domain))

            referrals: Sequence[ReferralEntity] = self.db_session.execute(stmt).scalars().all()
            return referrals

        except (SQLAlchemyError, TypeError, ValueError) as exc:
            raise exc

    def add_one(self, referral_entity: ReferralEntity) -> ReferralEntity:
        try:
            self.db_session.add(referral_entity)
            self.db_session.commit()
            return referral_entity
        except SQLAlchemyError as exc:
            self.db_session.rollback()
            raise exc

    def delete_one(self, referral_entity: ReferralEntity) -> None:
        try:
            self.db_session.delete(referral_entity)
            self.db_session.commit()
        except SQLAlchemyError as exc:
            self.db_session.rollback()
            raise exc
