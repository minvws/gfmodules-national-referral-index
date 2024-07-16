from typing import Any

from pydantic import BaseModel, field_validator, field_serializer

from app.data import ProviderID, Pseudonym, DataDomain

class ProviderRequest(BaseModel):
    pseudonym: Pseudonym
    data_domain: DataDomain

    @field_validator('pseudonym', mode='before')
    @classmethod
    def serialize_pseudonym(cls, val: str) -> Pseudonym:
        return Pseudonym(val)

    @field_validator('data_domain', mode='before')
    @classmethod
    def serialize_dd(cls, val: str) -> DataDomain:
        return DataDomain(val)


class Provider(BaseModel):
    provider_id: ProviderID
    pseudonym: Pseudonym
    data_domain: DataDomain

    @field_serializer('provider_id')
    def serialize_pi(self, provider_id: ProviderID) -> str:
        return str(provider_id)

    @field_serializer('data_domain')
    def serialize_dd(self, data_domain: DataDomain, _info: Any) -> str:
        return str(data_domain)

    @field_serializer('pseudonym')
    def serialize_ps(self, pseudonym: Pseudonym, _info: Any) -> str:
        return str(pseudonym)
