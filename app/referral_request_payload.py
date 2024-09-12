from app.response_models.referrals import ReferralEntry

class ReferrralLoggingPayload(ReferralEntry):
    requesting_uzi_number: str
    
    @classmethod
    def from_entry(cls, entry: ReferralEntry, uzi_number: str) -> "ReferrralLoggingPayload":
        return cls(ura_number=entry.ura_number, pseudonym=entry.pseudonym, data_domain=entry.data_domain, requesting_uzi_number=uzi_number)