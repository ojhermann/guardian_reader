from typing import Dict

from fastapi import APIRouter, Depends

from client.models.edition import Edition
from functions.services.editions.functions import get_editions
from functions.services.login.user_verification.functions import validate_token
from services.v1._client import guardian_client
from static_data.editions import EDITIONS

router = APIRouter(
    prefix=f"/{EDITIONS}",
    tags=[EDITIONS],
    dependencies=[Depends(validate_token)]
)

TAGS_METADATA: Dict[str, str] = {
    "name": f"{EDITIONS}",
}


@router.get("/", response_model=list[Edition])
async def get() -> list[Edition]:
    editions: list[Edition] = await get_editions(guardian_client)
    return editions
