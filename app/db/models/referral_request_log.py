from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.db.models.base import Base

class ReferralRequestLogEntry(Base):
    __tablename__ = 'referral_request_logs'

    ura_number: Mapped[str] = mapped_column("ura_number", String, primary_key=True)
    pseudonym: Mapped[str] = mapped_column("pseudonym", String, primary_key=True)
    data_domain: Mapped[str] = mapped_column("data_domain", String, primary_key=True)
    requesting_uzi_number: Mapped[str] = mapped_column("requesting_uzi_number", String)

    def __repr__(self) -> str:
        return f"<ReferralEntity(ura_number={self.ura_number}, pseudonym={self.pseudonym}, data_domain={self.pseudonym})"
