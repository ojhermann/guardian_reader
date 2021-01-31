from unittest import TestCase

from client.models.editions.editions import Editions
from test.test_client.test_models.test_editions.test_edition import edition

status: str = "ok"
user_tier: str = "fake_tier"
total: int = 1
editions: Editions = Editions(
    status=status,
    userTier=user_tier,
    total=total,
    results=[edition]
)


class TestEditions(TestCase):
    def test_it_has_status(self) -> None:
        self.assertEqual(status, editions.status)

    def test_it_has_user_tier(self) -> None:
        self.assertEqual(user_tier, editions.user_tier)

    def test_it_has_total(self) -> None:
        self.assertEqual(total, editions.total)

    def test_it_has_editions(self) -> None:
        self.assertEqual([edition], editions.editions)
