from pydantic_settings import BaseSettings, SettingsConfigDict

from .hf import HuggingFaceSettings
from .log import LogSettings
from .ui import UISettings
from .utils import UtilsSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        extra="ignore",
        env_prefix="WPP_AGENT__",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    DEBUG: bool = False

    LOG: LogSettings = LogSettings()
    HF: HuggingFaceSettings = HuggingFaceSettings()
    UI: UISettings = UISettings()
    UTILS: UtilsSettings = UtilsSettings()
