from typing import Any
from unittest import TestCase

from client.models.search.result import Result

from client.models.search.search_response import SearchResponse

EXAMPLE_JSON: dict[str, Any] = {
    "status": "ok",
    "userTier": "developer",
    "total": 2247005,
    "startIndex": 1,
    "pageSize": 1,
    "currentPage": 1,
    "pages": 2247005,
    "orderBy": "newest",
    "results": [
        {
            "id": "australia-news/live/2021/feb/04/daniel-andrews-tightens-covid-restrictions-after-australian-open-hotel-worker-tests-positive-australian-politics-live",
            "type": "liveblog",
            "sectionId": "australia-news",
            "sectionName": "Australia news",
            "webPublicationDate": "2021-02-03T23:34:27Z",
            "webTitle": "Daniel Andrews gives Victoria Covid update after Australian Open hotel worker tests positive – politics live",
            "webUrl": "https://www.theguardian.com/australia-news/live/2021/feb/04/daniel-andrews-tightens-covid-restrictions-after-australian-open-hotel-worker-tests-positive-australian-politics-live",
            "apiUrl": "https://content.guardianapis.com/australia-news/live/2021/feb/04/daniel-andrews-tightens-covid-restrictions-after-australian-open-hotel-worker-tests-positive-australian-politics-live",
            "isHosted": False,
            "pillarId": "pillar/news",
            "pillarName": "News"
        }
    ]
}

search_response: SearchResponse = SearchResponse(**EXAMPLE_JSON)


class TestSearchResponse(TestCase):
    def test_it_has_status(self) -> None:
        self.assertEqual(
            search_response.status,
            EXAMPLE_JSON.get("status")
        )

    def test_it_has_user_tier(self) -> None:
        self.assertEqual(
            search_response.user_tier,
            EXAMPLE_JSON.get("userTier")
        )

    def test_it_has_total_results(self) -> None:
        self.assertEqual(
            search_response.total_results,
            EXAMPLE_JSON.get("total")
        )

    def test_it_has_start_index(self) -> None:
        self.assertEqual(
            search_response.start_index,
            EXAMPLE_JSON.get("startIndex")
        )

    def test_it_has_results_per_response(self) -> None:
        self.assertEqual(
            search_response.start_index,
            EXAMPLE_JSON.get("pageSize")
        )

    def test_it_has_current_page(self) -> None:
        self.assertEqual(
            search_response.current_page,
            EXAMPLE_JSON.get("currentPage")
        )

    def test_it_has_total_pages(self) -> None:
        self.assertEqual(
            search_response.total_pages,
            EXAMPLE_JSON.get("pages")
        )

    def test_it_has_order_by(self) -> None:
        self.assertEqual(
            search_response.order_by,
            EXAMPLE_JSON.get("orderBy")
        )

    def test_it_has_results(self) -> None:
        self.assertEqual(
            search_response.results,
            [Result(**result) for result in EXAMPLE_JSON.get("results")]
        )
