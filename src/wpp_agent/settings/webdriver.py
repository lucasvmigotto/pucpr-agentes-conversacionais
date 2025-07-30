from typing import Self

from pydantic import BaseModel, HttpUrl, computed_field


class WebDriverSettings(BaseModel):
    URL: HttpUrl = HttpUrl("http://selenium:4444/wd/hub")

    @computed_field
    @property
    def remote_webdriver(self: Self) -> str:
        return self.URL.unicode_string()
