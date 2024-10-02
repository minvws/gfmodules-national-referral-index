
from sqlalchemy import insert

from app.db.decorator import repository
from app.db.models.referral_request_log import ReferralRequestLogEntry
from app.db.repository.respository_base import RepositoryBase
from app.referral_request_payload import ReferrralLoggingPayload


@repository(ReferralRequestLogEntry)
class ReferralRequestLoggingRepository(RepositoryBase):
    def add_one(self, payload: ReferrralLoggingPayload) -> None:
        stmt = insert(ReferralRequestLogEntry).values(
            ura_number=str(payload.ura_number), requesting_uzi_number=payload.requesting_uzi_number
        )
        self.db_session.execute(stmt)
        self.db_session.commit()
