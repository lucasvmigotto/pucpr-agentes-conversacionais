# pucpr-agentes-conversacionais

## Desenvolvimento

### Setup de ambiente

0. Você precisará ter instalado:

    * [Docker CE](https://docs.docker.com/engine/install/)
    * [DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
      * [Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
    * [Dev Cotainers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    * [API Key para Gemini](https://aistudio.google.com/app/apikey)

1. Clone do projeto

    ```bash
    git clone git@github.com:lucasvmigotto/pucpr-agentes-conversacionais.git
    ```

2. Copie o arquivo `.env.example` para `.env`

    > Altere e preencha os valores conforme necessário

3. Abra o projeto no Visual Studio Code e execute o comando `Dev Containers: Rebuild Container Without Cache`

### Comandos úteis

* Abrir um terminal dentro do container

    ```bash
    docker container exec -it $(docker container ls -aqf name=agentes-conversacionais) bash
    ```

* Iniciar a aplicação

    ```bash
    uv run app-run
    ```

## Deploy/Uso

1. Build da imagem Docker

    > Considerando o diretório atual sendo o mesmo do projeto

    ```bash
    docker build \
      --tag wpp-agent:latest \
      --file .docker/app.Dockerfile \
      --progress plain \
      --no-cache \
      .
    ```

2. Execução da aplicação

    > É imperativo a variável `WPP_AGENT__HF__GEMINI_API_TOKEN` estar presente e com um valor válido dentro do arquivo `.env`

    ```bash
    docker run \
      --rm \
      --interactive \
      --tty \
      --env-file .env \
      --mount "type=bind,src=./data,dst=/etc/agentes-conversacionais/data" \
      --mount "type=bind,src=./prompts,dst=/etc/agentes-conversacionais/prompts" \
      wpp-agent:latest
    ```

## Referências

* [Docs](https://docs.docker.com/get-started/)
* [Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
* [uv](https://docs.astral.sh/uv/)
* [Python: Settings](https://code.visualstudio.com/docs/python/settings-reference)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
