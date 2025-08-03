from pathlib import Path
from typing import Self

from pydantic import BaseModel, HttpUrl, computed_field


class HuggingFaceSettings(BaseModel):
    PROMPT_FOLDER_VALUE: str = "/etc/agentes-conversacionais/prompts/"

    AGENT_MAX_STEPS: int = 10

    GEMINI_API_URL: HttpUrl = HttpUrl(
        "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    GEMINI_API_TOKEN: str = "changeme"
    GEMINI_MODEL: str = "gemini-2.5-flash"

    @computed_field
    @property
    def prompt_folder(self: Self) -> Path:
        return Path(self.PROMPT_FOLDER_VALUE)

    @computed_field
    @property
    def gemini_api_url(self: Self) -> str:
        return self.GEMINI_API_URL.unicode_string()
