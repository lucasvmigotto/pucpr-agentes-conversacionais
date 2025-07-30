from pathlib import Path
from typing import Self

from pydantic import BaseModel, HttpUrl, computed_field


class HuggingFaceSettings(BaseModel):
    API_URL: HttpUrl = HttpUrl("https://router.huggingface.co/v1/chat/completions")

    AUTH_HEADER_KEY: str = "Authorization"
    TOKEN_TYPE: str = "Bearer"
    TOKEN_VALUE: str = "changeme"

    LLM_COMPLETIONS_MODEL: str = "deepseek-ai/DeepSeek-V3-0324:novita"

    SYSTEM_PROMPT_PATH: str = "/etc/agentes-conversacionais/prompt.md"

    LLM_INVALID_TOPIC: str = "N/A"
    LLM_INVALID_TOPIC_MESSAGE: str = (
        "Não consigo conversar sobre isso agora, desculpe..."
    )
    LLM_ERROR_MESSAGE: str = "Estou com um problema no momento, desculpe..."

    @computed_field
    @property
    def api_url(self: Self) -> str:
        return self.API_URL.unicode_string()

    @computed_field
    @property
    def auth_header(self: Self) -> dict[str, str]:
        return {self.AUTH_HEADER_KEY: f"{self.TOKEN_TYPE} {self.TOKEN_VALUE}"}

    @computed_field
    @property
    def system_prompt(self: Self) -> Path:
        return Path(self.SYSTEM_PROMPT_PATH)
