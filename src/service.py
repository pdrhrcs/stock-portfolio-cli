from typing import List
from src.model import Ativo

def calcular_carteira(ativos: List[Ativo]) -> List[Ativo]:
  for ativo in ativos:
    if ativo.preco_atual is not None:
      ativo.valor_total = ativo.quantidade * ativo.preco_atual
      ativo.lucro_reais = (ativo.preco_atual - ativo.preco_compra) * ativo.quantidade
      ativo.lucro_percentual = ((ativo.preco_atual - ativo.preco_compra) / ativo.preco_compra) * 100

  valor_total_carteira = sum(a.valor_total for a in ativos if a.valor_total is not None)
      
  for ativo in ativos:
    if valor_total_carteira > 0 and ativo.valor_total is not None:
      ativo.peso_carteira = (ativo.valor_total / valor_total_carteira) * 100

  return ativos
