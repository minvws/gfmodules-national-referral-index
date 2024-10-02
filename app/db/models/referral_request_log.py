from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.db.models.base import Base

class ReferralRequestLogEntry(Base):
    __tablename__ = 'referral_request_logs'

    id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)

    # TODO to add
    # request_type
    # endpoint
    # payload (JSON)
    
    ura_number: Mapped[str] = mapped_column("ura_number", String)
    requesting_uzi_number: Mapped[str] = mapped_column("requesting_uzi_number", String)