from typing import List, Dict

from fastapi import FastAPI

from services.v1.editions import router as editions_router, TAGS_METADATA as EDITIONS_TAGS_METADATA
from services.v1.login import router as login_router, TAGS_METADATA as LOGIN_TAGS_METADATA
from services.v1.search import router as search_router, TAGS_METADATA as SEARCH_TAGS_METADATA
from services.v1.sections import router as sections_router, TAGS_METADATA as SECTIONS_TAGS_METADATA

tags_metadata: List[Dict[str, str]] = [
    LOGIN_TAGS_METADATA,
    EDITIONS_TAGS_METADATA,
    SECTIONS_TAGS_METADATA,
    SEARCH_TAGS_METADATA,
]

app: FastAPI = FastAPI(
    title="Guardian Reader",
    openapi_tags=tags_metadata
)
app.include_router(login_router)
app.include_router(editions_router)
app.include_router(sections_router)
app.include_router(search_router)
