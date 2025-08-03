from pathlib import Path
from typing import Self

from pydantic import BaseModel, computed_field


class UtilsSettings(BaseModel):
    SEED: int = 42

    RAND_MIN: int = 1
    RAND_MAX: int = 3

    DATA_FOLDER_VALUE: str = "/etc/agentes-conversacionais/data/"

    @computed_field
    @property
    def rand_min_max_range(self: Self) -> tuple[int, int]:
        return self.RAND_MIN, self.RAND_MAX

    @computed_field
    @property
    def data_folder(self: Self) -> Path:
        return Path(self.DATA_FOLDER_VALUE)
