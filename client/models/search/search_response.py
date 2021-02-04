from pydantic import BaseModel, Field

from client.models.search.result import Result


class SearchResponse(BaseModel):
    """
    Response from The Guardian when using the search endpoint

    https://open-platform.theguardian.com/documentation/search
    """

    status: str = Field(
        ...,
        description="Guardian-specific http response code; it will return ok as long as the Guardian API received a well-formed request."
    )

    user_tier: str = Field(
        ...,
        description="Describes the type of rights possessed by the token used in the API call.",
        alias="userTier"
    )

    total_results: int = Field(
        ...,
        description="The total number of results",
        alias="total"
    )

    start_index: int = Field(
        ...,
        alias="startIndex"
    )

    results_per_response: int = Field(
        ...,
        description="Maximum number of results included in a resopnse",
        alias="pageSize",
    )

    current_page: int = Field(
        ...,
        description="Current page.",
        alias="currentPage"
    )

    total_pages: int = Field(
        ...,
        description="Number of pages given the results_per_response and total results.",
        alias="pages"
    )

    order_by: str = Field(
        ...,
        description="How the results are ordered.",
        alias="orderBy"
    )

    results: list[Result] = Field(
        ...,
        description="A list of Result objects."
    )
