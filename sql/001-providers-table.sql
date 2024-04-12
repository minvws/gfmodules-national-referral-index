CREATE TABLE providers (
      pseudonym VARCHAR(50) NOT NULL,
      provider_id VARCHAR(50) NOT NULL ,
      data_domain VARCHAR(100) NOT NULL,
      PRIMARY KEY (pseudonym, provider_id, data_domain)
);


INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('3e1806c5-f4b4-4e00-8b9b-9b0efb40d7a7', 'ziekenhuis.amsterdam@medmij', 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('3e1806c5-f4b4-4e00-8b9b-9b0efb40d7a7', 'ziekenhuis.amsterdam@medmij', 'test resultaten');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('3e1806c5-f4b4-4e00-8b9b-9b0efb40d7a7' , 'fysio.amsterdam@medmij' , 'test resultaten');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('16702733-a1cf-4395-87e6-d975cc3a2cf5', 'ziekenhuis.amsterdam@medmij' , 'beeldbank');
