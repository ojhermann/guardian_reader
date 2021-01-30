from fastapi import HTTPException, status


class InvalidPassword(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid password"
        )
