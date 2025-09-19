# 1 Bilhão de Linhas

## Descrição do Projeto

Este projeto é uma solução otimizada para o desafio de processar e analisar um arquivo CSV com um bilhão de linhas. A abordagem utiliza o **DuckDB**, um sistema de gerenciamento de banco de dados analítico in-process, para realizar consultas SQL diretas e eficientes nos dados, permitindo a análise de grandes volumes sem a necessidade de carregar todo o arquivo para a memória. O **Tqdm** é usado para fornecer feedback visual do progresso.

-----

## Instalação

Para começar, clone este repositório e instale as dependências usando o Poetry.

1.  Clone o repositório:
    ```bash
    git clone https://github.com/SamuelF15/1_bilhao_de_linhas.git
    cd 1-bilhao-de-linhas
    ```
2.  Defina a versão do Python usando o `pyenv local`:
    ```bash
    pyenv local 3.12.1
    ```
3.  Instale as dependências com Poetry:
    ```bash
    poetry env use 3.12.1
    poetry install --no-root
    poetry lock
    ```

Se você ainda não tem o Poetry instalado, siga as instruções no [site oficial](https://python-poetry.org/docs/#installation).

-----

## Uso

Para executar o projeto, use o comando `poetry run` seguido do nome do seu script. 

- poetry run src/nome.py

### Geração dos Dados

Primeiro, gere o arquivo `measurements.txt`:

```bash
poetry run python creat_csv.py
```

### Execução das Análises

Compare a performance executando cada script:

**1. Processamento com Python Puro**

```bash
poetry run python python_puro.py
```

**2. Processamento com DuckDB (CSV)**

```bash
poetry run python duck_csv.py
```

**3. Processamento com DuckDB (Parquet)**
*Converta o arquivo CSV para Parquet primeiro:*

```bash
poetry run python converter_parquet.py
```

*Em seguida, processe o novo arquivo:*

```bash
poetry run python duck_parquet.py
```

-----

## Autor

  * [Samuel Figueiredo](https://www.google.com/search?q=https://github.com/SamuelF15)

