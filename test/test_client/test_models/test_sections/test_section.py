from unittest import TestCase

from client.models.sections.edition import Edition
from client.models.sections.section import Section
from test.test_client.test_models.test_sections.test_edition import edition

id: str = "fake_id"
web_title: str = "fake_web_title"
api_url: str = "fake_api_url"
editions: list[Edition] = [edition]
section: Section = Section(
    id=id,
    webTitle=web_title,
    apiUrl=api_url,
    editions=editions
)


class TestSection(TestCase):
    def test_it_has_id(self) -> None:
        self.assertEqual(id, section.id)

    def test_it_has_web_title(self) -> None:
        self.assertEqual(web_title, section.web_title)

    def test_it_has_api_url(self) -> None:
        self.assertEqual(api_url, section.api_url)

    def test_it_has_editions(self) -> None:
        self.assertEqual(editions, section.editions)
