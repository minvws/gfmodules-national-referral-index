from unittest import TestCase

from app.config import set_config
from app.data import UraNumber, Pseudonym, DataDomain
from app.response_models.providers import Provider
from app.services.provider_service import ProviderService
from app.db.db import Database
from test_config import get_test_config


class ProviderServiceTest(TestCase):

    def setUp(self) -> None:
        set_config(get_test_config())
        # setup db
        self.db = Database("sqlite:///:memory:")
        self.db.generate_tables()
        # setup service
        self.provider_service = ProviderService(self.db)

    def test_db_connection(self) -> None:
        # act
        db_connection_valid = self.db.is_healthy()

        # assert
        self.assertEqual(db_connection_valid, True)

    def test_get_provider_by_domain_and_name(self) -> None:
        # arrange
        mock_provider = Provider(
            ura_number=UraNumber("12345"),
            pseudonym=Pseudonym("6d87d96a-cb78-4f5c-823b-578095da2c4a"),
            data_domain=DataDomain.BeeldBank
        )

        # act
        self.provider_service.add_one_provider(
            pseudonym=mock_provider.pseudonym,
            data_domain=mock_provider.data_domain,
            ura_number=mock_provider.ura_number,
        )
        actual_providers = self.provider_service.get_providers_by_domain_and_pseudonym(
            pseudonym=mock_provider.pseudonym, data_domain=mock_provider.data_domain
        )

        # assert
        for provider in actual_providers:
            self.assertEqual(provider.ura_number, mock_provider.ura_number)
            self.assertEqual(provider.pseudonym, mock_provider.pseudonym)
            self.assertEqual(provider.data_domain, mock_provider.data_domain)
