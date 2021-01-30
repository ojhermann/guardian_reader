from typing import Dict

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from functions.services.login.functions import generate_token
from models.login.token import Token
from static_data.login import LOGIN

router = APIRouter(
    prefix=f"/{LOGIN}",
    tags=[LOGIN]
)

TAGS_METADATA: Dict[str, str] = {
    "name": f"{LOGIN}",
}


@router.post("/", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Generates the token used to verify valid form data.
    """
    return await generate_token(form_data)
