from dataclasses import dataclass
from dataclasses import field
from typing import Optional

@dataclass
class Ativo:

  ticker: str
  quantidade: int
  preco_compra: float

  preco_atual: Optional[float] = field(default=None)
  valor_total: Optional[float] = field(default=None)
  lucro_reais: Optional[float] = field(default=None)
  lucro_percentual: Optional[float] = field(default=None)
  peso_carteira: Optional[float] = field(default=None)
