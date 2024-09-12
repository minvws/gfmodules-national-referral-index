
from app.db.repository.referral_request_logging_repository import ReferralRequestLoggingRepository
from app.db.session import DbSession
from .referral_request_logger import ReferralRequestLogger
from app.referral_request_payload import ReferrralLoggingPayload

class ReferralRequestDatabaseLogger(ReferralRequestLogger):
    _database_session: DbSession
    
    def __init__(self, database_session: DbSession) -> None:
        self._database_session = database_session
    
    def log(self, referral: ReferrralLoggingPayload) -> None:
        repo = ReferralRequestLoggingRepository(self._database_session)
        repo.add_one(referral)