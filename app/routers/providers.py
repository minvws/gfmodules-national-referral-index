import logging
from typing import List
from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from opentelemetry import trace
import textwrap

from uzireader.uziserver import UziServer

from app import container
from app.authentication import authenticated_ura
from app.data import UraNumber
from app.services.provider_service import ProviderService
from app.response_models.providers import ProviderRequest, Provider

logger = logging.getLogger(__name__)
router = APIRouter(
    tags=["Providers"],
)


@router.post(
    "/info",
    summary="Gets information about the provider by pseudonym and data domain",
    response_model=List[Provider],
)
def get_providers_info(
    request: Request,
    req: ProviderRequest,
    provider_service: ProviderService = Depends(container.get_provider_service),
    _: UraNumber = Depends(authenticated_ura)
) -> List[Provider]:
    """
    Searches for providers by pseudonym and data domain
    """
    span = trace.get_current_span()
    span.update_name(f"POST /info pseudonym={str(req.pseudonym)} data_domain={str(req.data_domain)}")

    providers = provider_service.get_providers_by_domain_and_pseudonym(
        pseudonym=req.pseudonym, data_domain=req.data_domain
    )
    span.set_attribute("data.providers_found", len(providers))

    if len(providers) == 0:
        raise HTTPException(status_code=404, detail="No provider found")

    span.set_attribute("data.providers", str(providers))

    return providers

