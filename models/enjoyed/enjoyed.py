from pydantic import BaseModel, Field


class Enjoyed(BaseModel):
    '''
    The id and date of when some content from The Guardian was enjoyed.
    '''
    as_of: int = Field(
        ...,
        description="Seconds since epoch of when the article was enjoyed."
    )

    id: str = Field(
        ...,
        description="Unique id."
    )
