from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str


class TokenResponseDataSchema(BaseModel):
    username: str | None = None
