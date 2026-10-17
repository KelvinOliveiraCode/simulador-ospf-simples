"""CLI de demonstração: imprime as tabelas de roteamento da rede."""

from __future__ import annotations

import sys

from .network import Link, Network, Router
from .routing import compute_routing_tables


def rede_exemplo() -> Network:
    rede = Network()
    for rid in ("R1", "R2", "R3", "R4"):
        rede.adicionar_roteador(Router(id=rid))
    links = [
        Link(origem="R1", destino="R2", custo=1),
        Link(origem="R2", destino="R3", custo=1),
        Link(origem="R3", destino="R4", custo=1),
        Link(origem="R1", destino="R4", custo=10),
    ]
    for link in links:
        rede.adicionar_link(link)
    return rede


def formatar_tabela(origem: str, tabela: dict) -> str:
    linhas = [f"Tabela de roteamento de {origem}:"]
    linhas.append("  destino  proximo_salto  custo")
    for destino in sorted(tabela):
        entrada = tabela[destino]
        linhas.append(
            f"  {destino:<8} {str(entrada.proximo_salto):<14} {entrada.custo_total}"
        )
    return "\n".join(linhas)


def main() -> int:
    rede = rede_exemplo()
    tabelas = compute_routing_tables(rede)
    for origem in sorted(tabelas):
        print(formatar_tabela(origem, tabelas[origem]))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
