from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    user_name: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ChangePasswordRequest(BaseModel):
    old_password: str

    new_password: str = Field(
        ...,
        min_length=6,
        max_length=72
    )    

class ResetPasswordRequest(BaseModel):
    new_password: str = Field(
        ...,
        min_length=6,
        max_length=72
    )    