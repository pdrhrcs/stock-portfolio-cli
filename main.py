import csv
from src.model import Ativo
from src.repository import buscar_preco_atual
from src.service import calcular_carteira
from src.view import exibir_carteira

def main():
  ativos = []

  with open('data/portfolio.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
      ativo = Ativo(
        ticker=linha['ticker'],
        quantidade=int(linha['quantidade']),
        preco_compra=float(linha['preco_compra'])
      )
      ativos.append(ativo)

  for ativo in ativos:
    try:
      ativo.preco_atual = buscar_preco_atual(ativo.ticker)
    except ValueError as e:
      print(f"Aviso: {e}")

  ativos = calcular_carteira(ativos)
  
  exibir_carteira(ativos)

if __name__ == "__main__":
  main()
