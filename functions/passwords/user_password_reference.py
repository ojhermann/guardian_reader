class UserPasswordReference(str):
    def __init__(
            self,
            username: str):
        super().__init__()

    def __new__(cls, username: str):
        return f"{username.upper()}_PASSWORD"
