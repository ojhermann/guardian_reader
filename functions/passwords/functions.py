from passlib.context import CryptContext

crypt_context: CryptContext = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def generate_password_hash(password: str) -> str:
    return crypt_context.hash(password)


def password_is_ok(
        password: str,
        password_hashed: str) -> bool:
    return crypt_context.verify(password, password_hashed)
