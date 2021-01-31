from unittest import TestCase

from client.models.editions.edition import Edition

id: str = "fake_id"
path: str = "path"
edition_title: str = "edition"
web_title: str = "fake_web_title"
web_url: str = "web_url"
api_url: str = "fake_api_url"
edition: Edition = Edition(
    id=id,
    path=path,
    edition=edition_title,
    webTitle=web_title,
    webUrl=web_url,
    apiUrl=api_url,
)


class TestEdition(TestCase):
    def test_it_contains_id(self) -> None:
        self.assertEqual(id, edition.id)

    def test_it_contains_path(self) -> None:
        self.assertEqual(path, edition.path)

    def test_it_contains_edition(self) -> None:
        self.assertEqual(edition_title, edition.edition)

    def test_it_contains_web_title(self) -> None:
        self.assertEqual(web_title, edition.web_title)

    def test_it_contains_web_url(self) -> None:
        self.assertEqual(web_url, edition.web_url)

    def test_it_contains_api_url(self) -> None:
        self.assertEqual(api_url, edition.api_url)
