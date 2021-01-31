from typing import Dict

from fastapi import APIRouter, Depends

from client.models.sections.section import Section
from client.models.sections.section_response import SectionResponse
from functions.services.login.user_verification.functions import validate_token
from services.v1._client import guardian_client
from static_data.sections import SECTIONS

router = APIRouter(
    prefix=f"/{SECTIONS}",
    tags=[SECTIONS],
    dependencies=[Depends(validate_token)]
)

TAGS_METADATA: Dict[str, str] = {
    "name": f"{SECTIONS}",
}


@router.get("/", response_model=list[Section])
async def get() -> list[Section]:
    section_response: SectionResponse = await guardian_client.get_sections()
    return section_response.sections
