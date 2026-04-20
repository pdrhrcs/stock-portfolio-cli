# Stock Portfolio CLI

CLI para análise de carteira de investimentos em tempo real, desenvolvida em Python.

## O que faz

Lê um arquivo CSV com os ativos da sua carteira e exibe uma tabela com preço atual, valor total, lucro/prejuízo em reais e percentual, e peso de cada ativo na carteira. Os dados são buscados em tempo real via yfinance, suportando ações brasileiras (B3) e americanas (NYSE/NASDAQ).

## Tecnologias

- Python 3.14.4
- yfinance
- pandas
- rich

## Como instalar

```bash
git clone https://github.com/pdrhrcs/stock-portfolio-cli.git
cd stock-portfolio-cli
pip install -r requirements.txt
```

## Como usar

Edite o arquivo `data/portfolio.csv` com seus ativos:

```csv
ticker,quantidade,preco_compra
PETR4.SA,100,28.50
AAPL,10,150.00
```

Ações brasileiras usam o sufixo `.SA`. Ações americanas não precisam de sufixo.

Execute:

```bash
python main.py
```

## Arquitetura

O projeto segue o padrão MVC:

- `model.py` >> estrutura de dados do Ativo
- `repository.py` >> busca de preços via yfinance
- `service.py` >> cálculos de lucro, valor e peso
- `view.py` >> exibição da tabela no terminal
- `main.py` >> orquestração do fluxo
