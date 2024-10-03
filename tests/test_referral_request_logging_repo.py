from unittest import TestCase

from app.config import set_config
from app.data import DataDomain, Pseudonym, UraNumber
from app.db.db import Database
from app.db.models.referral_request_log import ReferralRequestLogEntry
from app.db.repository.referral_request_logging_repository import (
    ReferralRequestLoggingRepository,
)
from app.db.session import DbSession
from app.referral_request_payload import ReferralLoggingPayload
from app.referral_request_type import ReferralRequestType
from tests.test_config import get_test_config

from sqlalchemy import select, func


TESTING_PSEUNONYM = Pseudonym("ea0b4ecf8d46479880a533252db21f1a")
TESTING_URA = UraNumber(123)

TESTING_DOMAIN = DataDomain.BeeldBank


class ReferralRequestLoggingRepositoryTest(TestCase):
    _repo: ReferralRequestLoggingRepository
    _session: DbSession

    def setUp(self) -> None:
        set_config(get_test_config())
        self._db = Database("sqlite:///:memory:")
        self._db.generate_tables()

        with self._db.get_db_session() as session:
            self._session = session

    def test_add(self):
        logging_payload = ReferralLoggingPayload(
            endpoint="https://test",
            requesting_uzi_number="123",
            ura_number=TESTING_URA,
            request_type=ReferralRequestType.CREATE,
            payload={},
        )

        repo = ReferralRequestLoggingRepository(self._session)
        repo.add_one(logging_payload)

        statement = select(func.count(ReferralRequestLogEntry.id))
        count = self._session.session.execute(statement).scalar()

        assert count == 1
