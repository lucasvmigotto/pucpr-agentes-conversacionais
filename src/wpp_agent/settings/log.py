from typing import Self

from pydantic import BaseModel, computed_field


class LogSettings(BaseModel):
    LEVEL: str = "DEBUG"
    DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    FORMAT: str = "{asctime} {levelname} {name}.{funcName}: {message}"
    STYLE: str = "{"

    @computed_field
    @property
    def config(self: Self) -> dict[str, str]:
        return {
            "level": self.LEVEL,
            "datefmt": self.DATE_FORMAT,
            "format": self.FORMAT,
            "style": self.STYLE,
        }
