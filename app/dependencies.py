from fastapi import Depends, Request
import inject
from app.data import UraNumber
from app.db.db import Database
from app.config import Config, load_default_config
from app.services.referral_service import ReferralService
from app.services.pseudonym_service import PseudonymService
from app.services.ura_number_finder import (
    ConfigOverridenURANumberFinder,
    StarletteRequestURANumberFinder,
)


def get_default_config() -> Config:
    return load_default_config()


def get_database() -> Database:
    return inject.instance(Database)


def get_referral_service() -> ReferralService:
    return inject.instance(ReferralService)


def get_pseudonym_service() -> PseudonymService:
    return inject.instance(PseudonymService)


def authenticated_ura(
    request: Request, config: Config = Depends(get_default_config)
) -> UraNumber:
    # I would also not use the injection framework for the URA number resolving.
    # The reason why is that the Starlette request is unknown at the time of object creation.
    #
    # The reason why I wouldn't advice an request parameter is because that will break the Liskov Substitution Principle (LSP);
    # the methods will not have the same signature. Instead, can simplify it here.
    finder = (
        ConfigOverridenURANumberFinder()
        if config.app.override_authentication_ura
        else StarletteRequestURANumberFinder(request)
    )
    return finder.find()
