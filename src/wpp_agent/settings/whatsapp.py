from typing import Self

from pydantic import BaseModel, HttpUrl, computed_field


class _WhatsAppCSSSelectors(BaseModel):
    MODAL_POPUP: str = "div[data-animate-modal-body] button"

    CONTACTS: str = "div[role=listitem]"
    UNREAD: str = "span[aria-label=Unread]"
    CONTACT_TITLE: str = "span[title]"

    INPUT: str = "div[contenteditable=true][data-tab='10']"
    SEND: str = "button[aria-label='Send']"

    MENU_BUTTON: str = "button[title=Menu][aria-label=Menu]"
    LOGOUT_BUTTON: str = "span[data-icon*=exit]"
    LOGOUT_MODAL_BUTTON: str = "div[aria-label='Log out?'] button:nth-child(2)"

    MESSAGES_IN: str = "div[class^=message-in] span[dir=ltr]"


class WhatsAppSettings(BaseModel):
    URL: HttpUrl = HttpUrl("https://web.whatsapp.com")

    QRCODE_PROMPT: str = "Scan the QR Code and press ENTER once ready"

    CONFIRM_SEND: str = "Press ENTER to send"

    CHAT_WITH_CONTACT: str = "John Doe"

    CSS: _WhatsAppCSSSelectors = _WhatsAppCSSSelectors()

    @computed_field
    @property
    def whatsapp_url(self: Self) -> str:
        return self.URL.unicode_string()
