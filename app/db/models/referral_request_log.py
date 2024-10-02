from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.db.models.base import Base
from app.referral_request_type import ReferralRequestType


class ReferralRequestLogEntry(Base):
    __tablename__ = "referral_request_logs"

    id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)

    # TODO to add
    # payload (JSON)

    endpoint: Mapped[str] = mapped_column("endpoint", String)

    # https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-python-enum-or-pep-586-literal-types-in-the-type-map
    request_type: Mapped[ReferralRequestType]

    ura_number: Mapped[str] = mapped_column("ura_number", String)
    requesting_uzi_number: Mapped[str] = mapped_column("requesting_uzi_number", String)
