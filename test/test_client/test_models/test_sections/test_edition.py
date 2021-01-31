from unittest import TestCase

from client.models.sections.edition import Edition

id: str = "fake_id"
web_title: str = "fake_web_title"
api_url: str = "fake_api_url"
code: str = "fake_code"
edition: Edition = Edition(
    id=id,
    webTitle=web_title,
    apiUrl=api_url,
    code=code)


class TestEdition(TestCase):
    def test_it_contains_id(self) -> None:
        self.assertEqual(id, edition.id)

    def test_it_contains_web_title(self) -> None:
        self.assertEqual(web_title, edition.web_title)

    def test_it_contains_api_url(self) -> None:
        self.assertEqual(api_url, edition.api_url)

    def test_it_contains_code(self) -> None:
        self.assertEqual(code, edition.code)
