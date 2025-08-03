from logging import Logger, getLogger
from sys import exit as exit_app

from ..agent import Agent
from ..settings import Settings


def init_agent_workflow(
    agent: Agent, settings: Settings, logger: Logger | None = None
) -> int:
    _log: Logger = logger or getLogger(__name__)
    try:
        user_input: str = input(settings.UI.initial_prompt)

        while True:
            if user_input.lower().strip() == "":
                user_input = input("Usuário: ")
                continue

            if user_input.lower().strip() == settings.UI.EXIT_KEYWORD:
                print(settings.UI.FINAL_PROMPT)
                break

            for message in agent(user_input):
                print(message)

            user_input: str = input("Usuário: ")

        exit_app(0)

    except KeyboardInterrupt:
        exit_app(0)

    except Exception as err:
        _log.exception(f"Error: {err}", exc_info=True)
        exit_app(1)
