# Projeto Aula — Trilha Python

O **Projeto Aula** é uma aplicação de linha de comando desenvolvida durante a
trilha de Python. A aplicação consulta a API [Useless Facts](https://uselessfacts.jsph.pl/)
para obter um fato aleatório em português e combina esse resultado com
informações do ambiente local.

## Funcionalidades

- Consulta fatos aleatórios em português por meio da API Useless Facts.
- Exibe o sistema operacional da execução.
- Exibe o diretório de trabalho atual.
- Exibe a data e a hora da execução em formato ISO 8601.
- Organiza a consulta à API e a coleta de informações do sistema em módulos
  separados.
- Disponibiliza testes automatizados para a função de consulta.

## Requisitos

- Python 3.11 ou superior.
- [Poetry](https://python-poetry.org/).
- Acesso à internet para consultar a API.

## Instalação

Clone o projeto, acesse a pasta e instale as dependências:

```bash
git clone <URL_DO_REPOSITORIO>
cd projeto_aula
poetry install
```

O comando `poetry install` instala as dependências de execução e as
dependências de desenvolvimento definidas no `pyproject.toml`.

## Execução

Execute a aplicação pelo script configurado no projeto:

```bash
poetry run projeto_aula
```

Também é possível executar o módulo diretamente:

```bash
poetry run python -m projeto_aula.main
```

O resultado é impresso como um dicionário semelhante a:

```text
{
    'fato': 'Um fato aleatório...',
    'sistema': 'win32',
    'diretorio': 'C:\\caminho\\do\\projeto',
    'data': '2026-10-19T16:05:05.648000'
}
```

O fato e a data variam a cada execução. O sistema e o diretório dependem do
ambiente em que o comando é executado.

## Testes e qualidade

Para executar os testes:

```bash
poetry run pytest
```

Para executar a verificação de lint e formatação:

```bash
poetry run task lint
```

Para formatar o código e corrigir imports:

```bash
poetry run task format
```

## Documentação local

A documentação é construída com MkDocs Material. Para abrir um servidor local
com atualização automática:

```bash
poetry run mkdocs serve
```

Depois, acesse `http://127.0.0.1:8000/` no navegador. Para gerar os arquivos
estáticos da documentação:

```bash
poetry run mkdocs build
```

## Estrutura principal

```text
.
├── docs/
│   └── index.md              # Página inicial da documentação
├── src/
│   └── projeto_aula/
│       ├── fatos.py          # Consulta e leitura do fato na API
│       ├── main.py           # Orquestração e ponto de entrada
│       └── sistema.py        # Coleta de informações do ambiente
├── tests/
│   └── unit/
│       └── test_unit.py      # Testes unitários
├── mkdocs.yml                # Configuração do MkDocs
├── poetry.lock               # Versões travadas das dependências
└── pyproject.toml            # Metadados, dependências e comandos
```

## API utilizada

A aplicação utiliza o endpoint de fatos aleatórios em português:

`https://uselessfacts.jsph.pl/api/v2/facts/random?language=pt`

A resposta esperada contém o campo `text`, que é usado como valor de `fato` no
resultado da aplicação.
