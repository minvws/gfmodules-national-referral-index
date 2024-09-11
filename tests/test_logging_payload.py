from app.data import DataDomain, Pseudonym, UraNumber
from app.referral_request_payload import ReferrralLoggingPayload
from app.response_models.referrals import ReferralEntry

TESTING_PSEUNONYM = Pseudonym('ea0b4ecf8d46479880a533252db21f1a')
TESTING_URA = UraNumber(123)

TESTING_DOMAIN = DataDomain.BeeldBank

def test_create_from_entry():
    entry = ReferralEntry(ura_number=TESTING_URA, pseudonym=TESTING_PSEUNONYM, data_domain=TESTING_DOMAIN)
    logging_payload = ReferrralLoggingPayload.from_entry(entry, '123')
    
    assert logging_payload.requesting_uzi_number == '123'