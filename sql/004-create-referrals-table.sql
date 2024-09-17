CREATE TABLE referral_request_logs (
    id SERIAL PRIMARY KEY,
    ura_number CHAR(9) NOT NULL,
    pseudonym VARCHAR(50) NOT NULL,
    data_domain VARCHAR(100) NOT NULL,
    requesting_uzi_number CHAR(9) NOT NULL
);