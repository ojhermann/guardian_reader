from unittest import TestCase

from functions.passwords.functions import generate_password_hash, password_is_ok


class TestFunctionsWork(TestCase):
    def test_they_work(self):
        passwords: list[str] = [
            "jasf;ljaoifjaos;jgl;asjgd",
            "lasjdfoiuwefl;`j;ioweoiu0982409sf",
            "opsudfoasjdfkajs0oiu24u0sodjv0s87)(*&(^)Y",
            "this_is_totally_some_password"
        ]

        for password in passwords:
            password_hash: str = generate_password_hash(password)
            self.assertTrue(password_is_ok(password, password_hash))
