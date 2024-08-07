from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    username: str
    email: str | None = None
