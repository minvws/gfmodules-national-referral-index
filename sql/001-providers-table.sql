CREATE TABLE providers (
      pseudonym VARCHAR(50) NOT NULL,
      ura_number VARCHAR(50) NOT NULL ,
      data_domain VARCHAR(100) NOT NULL,
      PRIMARY KEY (pseudonym, ura_number, data_domain)
);

ALTER TABLE providers OWNER TO localisation;
