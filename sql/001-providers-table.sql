CREATE TABLE providers (
      pseudonym VARCHAR(50) NOT NULL,
      provider_id VARCHAR(50) NOT NULL ,
      data_domain VARCHAR(100) NOT NULL,
      PRIMARY KEY (pseudonym, provider_id, data_domain)
);

ALTER TABLE providers OWNER TO localisation;

-- Mock: 950000012: 5afda8a1-dce9-43f8-b1af-c4dc765e7e17
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('5afda8a1-dce9-43f8-b1af-c4dc765e7e17', 'ziekenhuis.amsterdam@medmij', 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('5afda8a1-dce9-43f8-b1af-c4dc765e7e17', 'ziekenhuis.amsterdam@medmij', 'test resultaten');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('5afda8a1-dce9-43f8-b1af-c4dc765e7e17' , 'fysio.amsterdam@medmij' , 'test resultaten');

-- Mock: 950000024: cb5d785e-6710-4910-963f-39c85b39e491
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('cb5d785e-6710-4910-963f-39c85b39e491', 'ziekenhuis.amsterdam@medmij' , 'beeldbank');

-- Mock: 950000036: c41ef88d-9d06-4a81-9df8-a2b0f9534ab9
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('c41ef88d-9d06-4a81-9df8-a2b0f9534ab9', 'ziekenhuis.amsterdam@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('c41ef88d-9d06-4a81-9df8-a2b0f9534ab9', 'ziekenhuis.apeldoorn@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('c41ef88d-9d06-4a81-9df8-a2b0f9534ab9', 'huisarts.apeldoorn@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('c41ef88d-9d06-4a81-9df8-a2b0f9534ab9', 'fysio.deventetr@medmij' , 'beeldbank');

-- Mock: 950000048: 48521bd8-26a9-47d3-badc-c0190263c087
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('48521bd8-26a9-47d3-badc-c0190263c087', 'ziekenhuis.groningen@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('48521bd8-26a9-47d3-badc-c0190263c087', 'huisarts.groningen@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('48521bd8-26a9-47d3-badc-c0190263c087', 'huisarts.groningen@medmij' , 'test resultaten');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('48521bd8-26a9-47d3-badc-c0190263c087', 'huisarts.groningen@medmij' , 'medicatie');

-- Mock: 950000061: d8ee4fb0-e0e3-4a31-9255-2d140f86762e
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('d8ee4fb0-e0e3-4a31-9255-2d140f86762e', 'ziekenhuis.denbosch@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('d8ee4fb0-e0e3-4a31-9255-2d140f86762e', 'ziekenhuis.tilburg@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('d8ee4fb0-e0e3-4a31-9255-2d140f86762e', 'ziekenhuis.eindhoven@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('d8ee4fb0-e0e3-4a31-9255-2d140f86762e', 'huisarts.eindhoven@medmij' , 'beeldbank');
INSERT INTO public.providers (pseudonym, provider_id, data_domain) VALUES ('d8ee4fb0-e0e3-4a31-9255-2d140f86762e', 'huisarts.tilburg@medmij' , 'beeldbank');
