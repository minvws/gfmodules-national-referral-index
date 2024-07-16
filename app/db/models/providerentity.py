from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from app.db.models.base import Base


class ProviderEntity(Base):
    __tablename__ = 'providers'

    ura_number: Mapped[str] = mapped_column("ura_number", String, primary_key=True)
    pseudonym: Mapped[str] = mapped_column("pseudonym", String, primary_key=True)
    data_domain: Mapped[str] = mapped_column("data_domain", String, primary_key=True)

    def __repr__(self) -> str:
        return f"<Provider(ura_number={self.ura_number}, pseudonym={self.pseudonym}, data_domain={self.pseudonym})"
