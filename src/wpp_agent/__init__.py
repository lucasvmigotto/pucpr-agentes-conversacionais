from logging import Logger, getLogger
from sys import exit

from .app import init_agent_workflow
from .settings import Settings
from .setup import setup_app


def run_app(settings: Settings):
    setup_app(settings)
    _logger: Logger = getLogger(__name__)
    try:
        init_agent_workflow(settings)

    except KeyboardInterrupt:
        _logger.warning("CTRL+C, exiting app...")
        exit(0)

    except Exception as err:
        _logger.exception(f"Error: {err}", exc_info=True)
        exit(1)
