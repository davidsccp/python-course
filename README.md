
# Projeto: Pipeline de Limpeza e Transformação de Dados de Voos

Este projeto realiza uma pipeline de ETL simples usando Python para limpar, transformar e armazenar dados de voos em um banco SQLite. Os dados são carregados de uma fonte online, processados com base em metadados, e armazenados para análise futura.

## 📁 Estrutura do Projeto

```
projeto/
│
├── main.py                  # Arquivo principal para executar a pipeline
├── requirements.txt         # Dependências do projeto
├── assets/
│   └── metadado.xlsx        # Metadados para limpeza e tipagem das colunas
├── notebooks/
│   └── pipeline.ipynb 
│   └── DataClean.ipynb      # Notebooks para testes e desenvolvimento
└── src/
    ├── data_clean.py        # Classe para limpeza de dados
    ├── transform.py         # Funções para transformação de dados
    └── utils.py             # Funções utilitárias e criação de banco
```

## 🚀 Como executar

1. **Clone o repositório e acesse a pasta do projeto.**

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o pipeline:**

```bash
python main.py
```

## 📦 Fonte dos Dados

Os dados de voos são carregados diretamente de:

```
https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv
```

## 🛠 Funcionalidades

- Limpeza baseada em colunas obrigatórias e sem valores negativos
- Renomeação e tipagem automática das colunas via metadado
- Conversão de tempo de voo de minutos para horas
- Classificação de turno do dia baseado no horário do voo
- Criação automática da tabela no banco SQLite

## 📌 Observações

- A base SQLite `meu_banco.db` será criada na raiz do projeto.
- A tabela criada se chama `flights`.

---

