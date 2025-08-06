from functools import lru_cache
from typing import Any

from smolagents import tool

from ...utils import generate_sessions, load_movies, random_chance


@tool
@lru_cache
def list_movies() -> list[dict[str, Any]]:
    """Lista todos os filmes disponíveis, útil para
    buscar alguma informação sobre um filme que o usuário
    perguntou

    Returns:
        Lista com todos os filmes disponíveis
    """
    return [el.model_dump() for el in load_movies()]


@tool
@lru_cache
def list_sessions() -> list[dict[str, Any]]:
    """Lista todas as sessões disponíveis para um período de tempo.
    Útil para saber os filmes com sessões dentro de um determinado
    período de tempo.

    Returns:
        Lista com todas as sessões disponíveis
    """
    return [el.model_dump() for el in generate_sessions(load_movies())]


@tool
def buy_ticket(movie: str, session_time: str) -> str:
    """Compra de um ticket para uma sessão de cinema

    Args:
        movie: Nome do filme que se deseja comprar o ingresso
        session_time: Dia e horário da sessão do filme escolhido

    Returns:
        Confirmação se a compra pôde ser concluída ou não
    """
    if random_chance():
        return "Infelizmente essa sessão já foi vendida completamente"

    return "Compra realizada com sucesso"
