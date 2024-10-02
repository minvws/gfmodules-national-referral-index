import uuid
from app.data import DataDomain, Pseudonym, UraNumber
from app.referral_request_payload import ReferrralLoggingPayload
from app.referral_request_type import ReferralRequestType

TESTING_PSEUNONYM = Pseudonym(uuid.uuid4())
TESTING_URA = UraNumber(123)

TESTING_DOMAIN = DataDomain.BeeldBank


def test_create():
    logging_payload = ReferrralLoggingPayload(
        endpoint="https://test",
        requesting_uzi_number="123",
        ura_number=TESTING_URA,
        request_type=ReferralRequestType.GET,
        payload={},
    )

    assert logging_payload.requesting_uzi_number == "123"
