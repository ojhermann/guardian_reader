from unittest import TestCase

from models.enjoyed.enjoyed import Enjoyed

fake_as_of: int = 123456789
fake_id: str = "fake_id"

enjoyed: Enjoyed = Enjoyed(
    as_of=fake_as_of,
    id=fake_id
)


class TestEnjoyed(TestCase):
    def test_it_contains_as_of(self) -> None:
        self.assertEqual(fake_as_of, enjoyed.as_of)

    def test_it_contains_id(self) -> None:
        self.assertEqual(fake_id, enjoyed.id)
