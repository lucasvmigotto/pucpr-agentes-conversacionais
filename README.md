# pucpr-agentes-conversacionais

## Desenvolvimento

### Setup de ambiente

0. Você precisará ter instalado:

    * [Docker CE](https://docs.docker.com/engine/install/)
    * [DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
      * [Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
    * [Dev Cotainers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

1. Clone do projeto

    ```bash
    git clone git@github.com:lucasvmigotto/pucpr-agentes-conversacionais.git
    ```

2. Copie o arquivo `.env.example` para `.env`

    > Altere e preencha os valores conforme necessário

3. Crie a network Docker compartilhada:

    ```bash
    docker network create agentes-conversacionais
    ```

4. Abra o projeto no Visual Studio Code e execute o comando `Dev Containers: Rebuild Container Without Cache`

5. Inicie o serviço do Docker Compose `selenium`:

    ```bash
    docker compose up selenium
    ```

### Comandos úteis

* Abrir um terminal dentro do container

    ```bash
    docker container exec -it $(docker container ls -laqf) bash
    ```

* Iniciar e usar o Remove Web Driver

    ```bash
    uv run app-run
    ```

## Referências

* [Docs](https://docs.docker.com/get-started/)
* [Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
* [uv](https://docs.astral.sh/uv/)
* [Python: Settings](https://code.visualstudio.com/docs/python/settings-reference)
* [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
