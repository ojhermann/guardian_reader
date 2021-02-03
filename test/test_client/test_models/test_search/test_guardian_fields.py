from unittest import TestCase

from client.models.search.guardian_fields import GuardianFields
from test.test_client.test_models.test_search.test_result import EXAMPLE_JSON

guardian_fields: GuardianFields = GuardianFields(**EXAMPLE_JSON["fields"])


class TestGuardianFields(TestCase):
    def test_it_has_body(self) -> None:
        self.assertEqual(
            guardian_fields.body,
            EXAMPLE_JSON.get("fields").get("body")
        )
