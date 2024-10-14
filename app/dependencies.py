from fastapi import Depends, Request
import inject
from app.authentication import resolve_authenticated_ura_number
from app.data import UraNumber
from app.db.db import Database
from app.config import Config, load_default_config
from app.services.referral_service import ReferralService
from app.services.pseudonym_service import PseudonymService


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
    return resolve_authenticated_ura_number(request, config)
