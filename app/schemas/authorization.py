from typing import Optional
from pydantic import BaseModel


class Credentials(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
