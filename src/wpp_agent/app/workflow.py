from logging import Logger, getLogger

from ..settings import Settings
from ..utils import ask_reply, choice_accept
from .agent import Agent
from .whatsapp_webcrawler import WhatsAppWebCrawler


def init_agent_workflow(settings: Settings, logger: Logger | None = None) -> int:
    _logger: Logger = logger or getLogger(__name__)
    _agent = Agent(settings=settings.HF)

    with WhatsAppWebCrawler(settings) as crawler:
        crawler.open_whatsapp().wait(2).scan_qrcode().wait(2).handle_popup_modal().wait(
            3
        )

        while True:
            try:
                _logger.debug("Refreshing chats...")

                if len(chats := crawler.list_chats()) < 1:
                    _logger.debug("No chats found, waiting...")
                    crawler.wait(4)
                    continue

                for chat in chats:
                    chat.click()
                    from_who: str = crawler.get_chat_title(chat)

                    if (last_message := crawler.last_message_in()) is None:
                        _logger.debug(f"No messages received from {from_who}")
                        continue

                    if not choice_accept(ask_reply(from_who, last_message)):
                        continue

                    if (
                        llm_answer := _agent.answer_message(last_message)
                    ) == settings.HF.LLM_INVALID_TOPIC:
                        crawler.type_message(
                            settings.HF.LLM_INVALID_TOPIC_MESSAGE
                        ).wait(2)

                    crawler.type_message(llm_answer).wait(2)
                    crawler.send_message()

            except KeyboardInterrupt:
                break

        crawler.logout()
