from logging import Logger, getLogger
from typing import Generator, Self

from smolagents import (
    ActionStep,
    ChatMessageStreamDelta,
    FinalAnswerStep,
    OpenAIModel,
    PlanningStep,
    ToolCall,
    ToolCallingAgent,
)
from smolagents.tools import Tool

from ..settings import HuggingFaceSettings, Settings
from .tool import buy_ticket, list_movies, list_sessions


class Agent:
    @staticmethod
    def _load_system_prompt(settings: HuggingFaceSettings) -> str | None:
        if not (prompt_file := settings.prompt_folder / "system.md").exists():
            return None

        with open(prompt_file) as file_ref:
            return file_ref.read()

    @staticmethod
    def _init_gemini_client(settings: HuggingFaceSettings) -> OpenAIModel:
        return OpenAIModel(
            model_id=settings.GEMINI_MODEL,
            api_base=settings.gemini_api_url,
            api_key=settings.GEMINI_API_TOKEN,
        )

    @staticmethod
    def _init_tool_calling_agent(
        client: OpenAIModel,
        /,
        *tools: Tool,
        settings: HuggingFaceSettings,
    ) -> ToolCallingAgent:
        return ToolCallingAgent(
            model=client,
            tools=tools,
            max_steps=settings.AGENT_MAX_STEPS,
            instructions=Agent._load_system_prompt(settings),
        )

    def __init__(self: Self, settings: Settings):
        self._log: Logger = getLogger(__name__)
        self._client: OpenAIModel = Agent._init_gemini_client(settings.HF)
        self._agent: ToolCallingAgent = Agent._init_tool_calling_agent(
            self._client, buy_ticket, list_sessions, list_movies, settings=settings.HF
        )

    def __call__(
        self: Self, message: str
    ) -> Generator[
        str,
        None,
        None,
    ]:
        for chunk in self._agent.run(message, stream=True):
            if not isinstance(chunk, FinalAnswerStep):
                self._log.debug(chunk)
                continue

            yield chunk.output
