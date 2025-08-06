# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:python3.12-bookworm AS builder

WORKDIR /build

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
        --frozen \
        --no-install-project \
        --no-editable \
        --compile-bytecode \
        --no-dev

FROM python:3.12-slim-bookworm AS app

WORKDIR /app

COPY \
    --from=builder \
    --chown=app:app \
    /build/.venv/ \
    /app/.venv/

COPY \
    ./src/wpp_agent/ \
    /app/wpp_agent/

VOLUME "/etc/agentes-conversacionais/"

ENTRYPOINT [ "/app/.venv/bin/python"]

CMD [ "-m", "wpp_agent" ]
