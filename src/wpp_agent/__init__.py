from logging import getLogger

from .agent import Agent
from .app import init_agent_workflow
from .settings import Settings
from .setup import setup_app


def run_app(settings: Settings) -> None:
    setup_app(settings)
    init_agent_workflow(Agent(settings), settings, getLogger(__name__))
