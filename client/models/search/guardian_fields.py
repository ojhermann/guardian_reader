from typing import Optional

from pydantic import BaseModel, Field


class GuardianFields(BaseModel):
    body: Optional[str] = Field(
        ...,
        description="HTML of the related article."
    )
