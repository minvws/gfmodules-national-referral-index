from dataclasses import dataclass
from typing import Any
from app.data import UraNumber
from app.referral_request_type import ReferralRequestType
from app.response_models.referrals import ReferralEntry

@dataclass
class ReferrralLoggingPayload:
    endpoint: str
    requesting_uzi_number: str   
    ura_number: UraNumber
    request_type: ReferralRequestType
    payload: dict[str, Any]

    @classmethod
    def from_entry(cls, entry: ReferralEntry, uzi_number: str) -> "ReferrralLoggingPayload":
        return cls(ura_number=entry.ura_number, requesting_uzi_number=uzi_number)