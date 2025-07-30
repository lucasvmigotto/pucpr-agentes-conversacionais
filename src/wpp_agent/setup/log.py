from logging import Handler, basicConfig

from ..settings import Settings


def setup_log(settings: Settings) -> None:
    handlers: list[Handler] = []

    if settings.DEBUG:
        try:
            from rich.logging import RichHandler
        except ImportError:
            print("rich formatter not found")
            exit(1)

        handlers.append(RichHandler())

    basicConfig(
        handlers=handlers,
        **settings.LOG.config,  # type: ignore
    )
