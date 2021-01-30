from unittest import TestCase

from functions.passwords.user_password_reference import UserPasswordReference


class TestUserPasswordReference(TestCase):
    def test_it_works(self):
        names: list[str] = ["albert", "bogdan", "clarissa", "denice", "evelyn", "farah"]
        expected_results: list[str] = [name.upper() + "_PASSWORD" for name in names]
        for expected_result, name in zip(expected_results, names):
            self.assertEqual(expected_result, UserPasswordReference(name))
