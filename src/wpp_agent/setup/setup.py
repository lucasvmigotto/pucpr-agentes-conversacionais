from typing import Callable, Unpack

from pydantic import BaseModel

from ..settings import Settings, settings
from .log import setup_log

_SETUP_FUNCTIONS: dict[str, Callable] = {
    "log": setup_log,
}


class SetUpFunctions(BaseModel):
    log: bool = True


def setup_app(settings: Settings = settings, **modules: Unpack[SetUpFunctions]) -> None:
    for func, _ in filter(
        lambda el: el[-1], (SetUpFunctions().model_dump() | modules).items()
    ):
        _SETUP_FUNCTIONS[func](settings)
