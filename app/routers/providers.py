import logging
from typing import Sequence, List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from opentelemetry import trace

from app import container
from app.db.models.provider import Provider
from app.services.provider_service import ProviderService
from app.response_models.providers import ProvidersRequest, ProvidersResponse

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/info",
    summary="Gets information about the provider by pseudonym and data domain",
    tags=["Providers"],
    response_model=List[ProvidersResponse],
)
async def get_providers_info(
    data: ProvidersRequest,
    provider_service: ProviderService = Depends(container.get_provider_service),
) -> Sequence[Provider]:

    span = trace.get_current_span()
    span.update_name(f"POST /info pseudonym={data.pseudonym} data_domain={data.data_domain}")

    providers = provider_service.get_providers_by_domain_and_pseudonym(
        pseudonym=data.pseudonym, data_domain=data.data_domain
    )
    span.set_attribute("data.providers_found", len(providers))

    if len(providers) == 0:
        raise HTTPException(status_code=404, detail="No provider found")

    span.set_attribute("data.providers", str(providers))
    return providers
