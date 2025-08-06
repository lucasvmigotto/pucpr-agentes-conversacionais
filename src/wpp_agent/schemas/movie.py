from enum import StrEnum

from pydantic import Field

from ._base import _BaseSchema


class MovieCategory(StrEnum):
    COMEDY = "Comédia"
    ACTION = "Ação"
    ROMANCE = "Romance"
    DOC = "Documentário"
    THRILLER = "Terror"
    DRAMA = "Drama"


class Movie(_BaseSchema):
    title: str = Field(description="Título do filme")
    synopsis: str = Field(description="Sinópse do filme")
    category: MovieCategory = Field(description="Categoria do gênero do filme")
    release_year: int = Field(description="Ano de lançamento")


class Session(_BaseSchema):
    movie: Movie = Field(description="Filme que será exibido")
    datetime: str = Field(description="Data e hora da sessão")
