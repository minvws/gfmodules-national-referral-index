from dataclasses import dataclass
from app.data import UraNumber
from app.response_models.referrals import ReferralEntry

@dataclass
class ReferrralLoggingPayload:
    requesting_uzi_number: str   
    ura_number: UraNumber

    @classmethod
    def from_entry(cls, entry: ReferralEntry, uzi_number: str) -> "ReferrralLoggingPayload":
        return cls(ura_number=entry.ura_number, requesting_uzi_number=uzi_number)