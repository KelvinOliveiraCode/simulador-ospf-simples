"""Simulador OSPF simplificado com tabela de roteamento.

Modelo de rede (roteadores e links com custo), algoritmo de caminho
mínimo determinístico (Dijkstra) e geração de tabela de roteamento por
roteador. Sem dependências externas: apenas a biblioteca padrão do Python.
"""

from .dijkstra import dijkstra
from .network import Link, Network, Router
from .routing import RouteEntry, compute_routing_tables

__all__ = [
    "Link",
    "Network",
    "Router",
    "RouteEntry",
    "compute_routing_tables",
    "dijkstra",
]

__version__ = "0.1.0"
