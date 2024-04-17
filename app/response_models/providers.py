from pydantic import BaseModel


class ProvidersRequest(BaseModel):
    pseudonym: str
    data_domain: str


class ProvidersResponse(BaseModel):
    provider_id: str
    pseudonym: str
    data_domain: str

    class Config:
        from_attribute = True
