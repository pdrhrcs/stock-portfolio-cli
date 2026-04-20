from rich.table import Table
from rich.console import Console
from typing import List
from src.model import Ativo

def exibir_carteira(ativos: List[Ativo]) -> None:
  console = Console()
  tabela = Table(title="Carteira de Investimentos")

  tabela.add_column("Ticker", justify="left", style="cyan", no_wrap=True)
  tabela.add_column("Quantidade", justify="right", style="magenta")
  tabela.add_column("Preço Compra", justify="right", style="green")
  tabela.add_column("Preço Atual", justify="right", style="green")
  tabela.add_column("Valor Total", justify="right", style="yellow")
  tabela.add_column("Lucro (R$)", justify="right", style="red")
  tabela.add_column("Lucro (%)", justify="right", style="red")
  tabela.add_column("Peso Carteira (%)", justify="right", style="blue")

  for ativo in ativos:
    if ativo.lucro_reais is not None:
      cor_lucro = "green" if ativo.lucro_reais >= 0 else "red"
      lucro_reais_str = f"[{cor_lucro}]R$ {ativo.lucro_reais:.2f}[/{cor_lucro}]"
    else:
      lucro_reais_str = "N/A"
    if ativo.lucro_percentual is not None:
      cor_pct = "green" if ativo.lucro_percentual >= 0 else "red"
      lucro_pct_str = f"[{cor_pct}]{ativo.lucro_percentual:.2f}%[/{cor_pct}]"
    else:
      lucro_pct_str = "N/A"

    tabela.add_row(
      ativo.ticker,
      str(ativo.quantidade),
      f"R$ {ativo.preco_compra:.2f}",
      f"R$ {ativo.preco_atual:.2f}" if ativo.preco_atual is not None else "N/A",
      f"R$ {ativo.valor_total:.2f}" if ativo.valor_total is not None else "N/A",
      lucro_reais_str,
      lucro_pct_str,
      f"{ativo.peso_carteira:.2f}%" if ativo.peso_carteira is not None else "N/A"
    )

  console.print(tabela)
