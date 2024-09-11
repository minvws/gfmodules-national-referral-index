from typing import List

from app.data import Pseudonym, DataDomain, UraNumber
from app.db.db import Database
from app.db.models.referral import ReferralEntity
from app.db.repository.referral_repository import ReferralRepository
from app.referral_request_database_logger import ReferralRequestDatabaseLogger
from app.referral_request_payload import ReferrralLoggingPayload
from app.response_models.referrals import ReferralEntry


class ReferralService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def get_referrals_by_domain_and_pseudonym(
        self, pseudonym: Pseudonym, data_domain: DataDomain
    ) -> List[ReferralEntry]:
        """
        Method that gets all the referrals by pseudonym and data domain
        """
        with self.database.get_db_session() as session:
            referral_repository = session.get_repository(ReferralRepository)
            entities = referral_repository.find_many_referrals(pseudonym, data_domain)

            return [self.hydrate_referral(entity) for entity in entities]

    def add_one_referral(
        self, pseudonym: Pseudonym, data_domain: DataDomain, ura_number: UraNumber, uzi_number: str
    ) -> ReferralEntry:
        with self.database.get_db_session() as session:
            referral_repository = session.get_repository(ReferralRepository)
            referral_repository.add_one(
                pseudonym=pseudonym, data_domain=data_domain, ura_number=ura_number
            )
            logging_payload = ReferrralLoggingPayload(ura_number=ura_number, pseudonym=pseudonym, data_domain=data_domain, requesting_uzi_number=uzi_number)
            
            logger= ReferralRequestDatabaseLogger(session)
            logger.log(logging_payload)

        return ReferralEntry(
            ura_number=ura_number,
            pseudonym=pseudonym,
            data_domain=data_domain,
        )

    @staticmethod
    def hydrate_referral(entity: ReferralEntity) -> ReferralEntry:
        data_domain = DataDomain.from_str(entity.data_domain)
        if data_domain is None:
            raise ValueError("Invalid data domain")

        return ReferralEntry(
            ura_number=UraNumber(entity.ura_number),
            pseudonym=Pseudonym(entity.pseudonym),
            data_domain=data_domain,
        )
