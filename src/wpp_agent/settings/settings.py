from pydantic_settings import BaseSettings, SettingsConfigDict

from .log import LogSettings
from .webdriver import WebDriverSettings
from .whatsapp import WhatsAppSettings


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
    WEBDRIVER: WebDriverSettings = WebDriverSettings()
    WPP: WhatsAppSettings = WhatsAppSettings()
