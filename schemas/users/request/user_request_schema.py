from pydantic import BaseModel


class UserRequestSchema(BaseModel):
    username: str
    email: str | None = None
