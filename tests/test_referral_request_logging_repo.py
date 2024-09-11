from unittest import TestCase

from app.config import set_config
from app.data import DataDomain, Pseudonym, UraNumber
from app.db.db import Database
from app.db.models.referral_request_log import ReferralRequestLogEntry
from app.db.repository.referral_request_logging_repository import ReferralRequestLoggingRepository
from app.db.session import DbSession
from app.referral_request_payload import ReferrralLoggingPayload
from app.response_models.referrals import ReferralEntry
from tests.test_config import get_test_config


TESTING_PSEUNONYM = Pseudonym('ea0b4ecf8d46479880a533252db21f1a')
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
        entry = ReferralEntry(ura_number=TESTING_URA, pseudonym=TESTING_PSEUNONYM, data_domain=TESTING_DOMAIN)
        logging_payload = ReferrralLoggingPayload.from_entry(entry, '123')
        
        repo = ReferralRequestLoggingRepository(self._session)
        repo.add_one(logging_payload)
        
        count = self._session.session.query(ReferralRequestLogEntry).count()
        
        assert count == 1
