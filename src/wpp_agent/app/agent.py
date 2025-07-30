from logging import Logger, getLogger
from pathlib import Path
from typing import Self

from requests import post as req_post

from ..schemas import HFCompletionPayload, HFMessage
from ..settings import HuggingFaceSettings


class Agent:
    @staticmethod
    def _load_system_prompt(prompt_path: Path | str) -> str:
        content: str = ""

        with open(prompt_path) as file_ref:
            content = file_ref.read()
            file_ref.close()

        if content.count("{user_message}") < 1:
            raise Exception(
                f"Prompt inside {prompt_path} does not have template entry for 'user_message'"
            )

        return content

    def __init__(self: Self, settings: HuggingFaceSettings):
        self._logger: Logger = getLogger(__name__)
        self._settings = settings
        self._system_prompt: str = self._load_system_prompt(
            self._settings.system_prompt
        )

    def _format_message(self: Self, message: str) -> str:
        return self._system_prompt.format(user_message=message)

    def _build_messages_payload_from_message(
        self: Self, message: str
    ) -> HFCompletionPayload:
        return HFCompletionPayload(
            model=self._settings.LLM_COMPLETIONS_MODEL,
            messages=[HFMessage(content=self._format_message(message))],
        )

    def answer_message(self: Self, message: str) -> str:
        try:
            (
                response := req_post(
                    url=self._settings.api_url,
                    json=self._build_messages_payload_from_message(
                        message
                    ).model_dump(),
                    headers=self._settings.auth_header,
                )
            ).raise_for_status()

            completion: str = response.json()["choices"][0]["message"]["content"]

            return completion

        except Exception as err:
            self._logger.exception(f"Error: {err}", exc_info=True)
            return self._settings.LLM_ERROR_MESSAGE
