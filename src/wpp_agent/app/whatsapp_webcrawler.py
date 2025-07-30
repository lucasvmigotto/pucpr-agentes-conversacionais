from logging import Logger, getLogger
from time import sleep
from typing import Self

from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ..settings import Settings


class WhatsAppWebCrawler:
    def __init__(self: Self, settings: Settings):
        self._logger: Logger = getLogger(__name__)
        self._settings = settings
        self._driver: RemoteWebDriver | None = None

    @property
    def driver(self: Self) -> RemoteWebDriver | None:
        return self._driver

    def __enter__(self: Self) -> Self:
        self._driver = RemoteWebDriver(
            command_executor=self._settings.WEBDRIVER.remote_webdriver,
            options=ChromeOptions(),
        )
        return self

    def __exit__(self: Self, *errs):
        if any(errs):
            self._logger.error("\n".join([f"Err: {err}" for err in errs]))

        if self._driver is not None:
            self._driver.quit()

    def query_element(self: Self, css_query: str) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, css_query)

    def query_elements(self: Self, css_query: str) -> list[WebElement]:
        return self._driver.find_elements(By.CSS_SELECTOR, css_query)

    def found_element(self: Self, css_query) -> WebElement:
        if (element := self.query_element(css_query)) is None:
            raise Exception(f"Element ({css_query}) not found")
        return element

    def wait(self: Self, seconds: int) -> Self:
        sleep(seconds)
        return self

    def open_whatsapp(self: Self) -> Self:
        self._logger.debug("Opening WhatsApp")
        self._driver.get(self._settings.WPP.whatsapp_url)
        self._driver.maximize_window()
        return self

    def scan_qrcode(self: Self) -> Self:
        self._logger.debug("Waiting QR Code scan")
        _: str = input(self._settings.WPP.QRCODE_PROMPT)
        return self

    def handle_popup_modal(self: Self) -> Self:
        self._logger.debug("Checking for popup modal")
        if (
            popup_modal := self.query_element(self._settings.WPP.CSS.MODAL_POPUP)
        ) is not None:
            self._logger.debug("Popup modal found")
            popup_modal.click()
        else:
            self._logger.debug("Popup modal not found")

        return self

    def list_chats(self: Self) -> list[WebElement]:
        return self.query_elements(self._settings.WPP.CSS.CONTACTS)

    def get_chat_title(self: Self, element: WebElement) -> str:
        return element.find_element(
            By.CSS_SELECTOR, self._settings.WPP.CSS.CONTACT_TITLE
        ).text

    def pick_chat(self: Self, title: str, chats: list[WebElement]) -> WebElement | None:
        for chat in chats:
            if self.get_chat_title(chat).count(title) > 0:
                return chat

        return None

    def type_message(self: Self, message: str) -> Self:
        input_selector: str = self._settings.WPP.CSS.INPUT

        input_field: WebElement = self.found_element(input_selector)
        input_field.click()
        input_field.send_keys(message)

        return self

    def send_message(self: Self, confirm: bool = False) -> Self:
        send_button: WebElement = self.found_element(self._settings.WPP.CSS.SEND)

        if confirm:
            _confirm_message: str = self._settings.WPP.CONFIRM_SEND
            self._logger.warning(_confirm_message)
            input(_confirm_message)

        send_button.click()

        return self

    def load_messages(self: Self) -> list[WebElement]:
        return self.query_elements(self._settings.WPP.CSS.MESSAGES_IN)

    def last_message_in(self: Self) -> str | None:
        return messages[-1].text if len(messages := self.load_messages()) > 0 else None

    def logout(self: Self) -> Self:
        self.found_element(self._settings.WPP.CSS.MENU_BUTTON).click()
        self.wait(1)
        self.found_element(self._settings.WPP.CSS.LOGOUT_BUTTON).click()
        self.wait(3)
        self.found_element(self._settings.WPP.CSS.LOGOUT_MODAL_BUTTON).click()
        self.wait(3)
        return self
