from typing import Literal

from pydantic import BaseModel


class HFMessage(BaseModel):
    role: Literal["user"] = "user"
    content: str


class HFCompletionPayload(BaseModel):
    model: str
    messages: list[HFMessage]
