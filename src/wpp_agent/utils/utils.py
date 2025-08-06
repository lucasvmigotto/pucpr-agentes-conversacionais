from datetime import datetime as dt
from datetime import timedelta as td
from json import load
from typing import Sequence

from numpy.random import randint
from numpy.random import randint as np_randint

from ..schemas import Movie, Session
from ..settings import settings


def random_chance() -> bool:
    return randint(*settings.UTILS.rand_min_max_range) % 2 == 0


def load_movies() -> list[Movie]:
    movies: list[Movie] = []

    with open(settings.UTILS.data_folder / "movies.json") as file_ref:
        movie_data = load(file_ref)

        for movie in movie_data:
            movies.append(Movie(**movie))

        file_ref.close()

        return movies


def _rand_session_time(
    date: dt,
    hour_range_min: int = 9,
    hour_range_max: int = 23,
    datetime_mask: str = "%Y-%m-%d %H:%M:%s",
) -> dt:
    return date.replace(
        hour=np_randint(hour_range_min, hour_range_max + 1),
        minute=0,
        second=0,
        microsecond=0,
    ).strftime(datetime_mask)


def generate_sessions(
    movie_list: Sequence[Movie] = None,
    n_days: int = 7,
    movies_a_day: int = 8,
    include_today: bool = True,
) -> list[Session]:
    days = [dt.today() + td(days=n_day) for n_day in range(1, n_days + 1)]

    if include_today:
        days = [dt.today()] + days

    sessions: list[Session] = []

    movie_list_len: int = len(movie_list)

    for day in days:
        _movies = [
            movie_list[np_randint(0, movie_list_len)] for _ in range(movies_a_day)
        ]
        _movies_len = len(_movies)
        for _ in range(movies_a_day):
            sessions.append(
                Session(
                    movie=_movies[np_randint(0, _movies_len)],
                    datetime=_rand_session_time(day),
                )
            )

    return sessions
