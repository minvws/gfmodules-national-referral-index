import abc

from app.referral_request_payload import ReferrralLoggingPayload

class ReferralRequestLogger(abc.ABC):
    @abc.abstractmethod
    def log(self, referral: ReferrralLoggingPayload) -> None:
        ...