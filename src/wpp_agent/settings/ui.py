from typing import Self

from pydantic import BaseModel, computed_field


class UISettings(BaseModel):
    EXIT_KEYWORD: str = "sair"

    INITIAL_PROMPT: str = (
        'Como posso te ajudar hoje?\n(Digite "##exit_keyword##",'
        ' ou pressione "CTRL+C" para parar a conversa'
        " a qualquer momento)\n"
        "Usuário: "
    )

    FINAL_PROMPT: str = "Até mais!"

    @computed_field
    @property
    def initial_prompt(self: Self) -> str:
        return self.INITIAL_PROMPT.replace("##exit_keyword##", self.EXIT_KEYWORD)
