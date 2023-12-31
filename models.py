from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None


class UserInDB(User):
    hash_password: str
class Toke(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

