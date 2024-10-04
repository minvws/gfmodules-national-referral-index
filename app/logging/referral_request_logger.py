import abc

from app.referral_request_payload import ReferralLoggingPayload


class ReferralRequestLogger(abc.ABC):
    @abc.abstractmethod
    def log(self, referral: ReferralLoggingPayload) -> None:
        ...
