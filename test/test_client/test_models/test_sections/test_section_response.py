from unittest import TestCase

from client.models.sections.section import Section
from client.models.sections.section_response import SectionResponse
from test.test_client.test_models.test_sections.test_section import section

status: str = "ok"
user_tier: str = "fake_tier"
section_count: int = 1
sections: list[Section] = [section]
section_response: SectionResponse = SectionResponse(
    status=status,
    userTier=user_tier,
    total=section_count,
    results=sections
)


class TestSectionResponse(TestCase):
    def it_has_status(self) -> None:
        self.assertEqual(status, section_response.status)

    def it_has_user_tier(self) -> None:
        self.assertEqual(user_tier, section_response.user_tier)

    def it_has_section_count(self) -> None:
        self.assertEqual(section_count, section_response.section_count)

    def it_has_sections(self) -> None:
        self.assertEqual(sections, section_response.sections)
