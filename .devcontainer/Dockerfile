# syntax=docker/dockerfile:1.7-labs

FROM mcr.microsoft.com/devcontainers/python:3.12

ARG USERNAME="vscode"

ENV VIRTUAL_ENV="/home/${USERNAME}/venv"
ENV UV_PROJECT_ENVIRONMENT="${VIRTUAL_ENV}"
ENV UV_LINK_MODE="copy"

USER "${USERNAME}"

RUN mkdir -p "${VIRTUAL_ENV}"

COPY --from=ghcr.io/astral-sh/uv:latest \
    /uv /uvx \
    /bin/

WORKDIR /code

RUN cat <<EOF >> ~/.bashrc
if [[ -d $HOME/venv/bin/ ]]; then
    . $HOME/venv/bin/activate
fi
EOF

VOLUME "${VIRTUAL_ENV}"
VOLUME "/etc/agentes-conversacionais/"
