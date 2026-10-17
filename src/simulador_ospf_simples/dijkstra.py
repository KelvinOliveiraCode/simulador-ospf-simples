"""Algoritmo de caminho mínimo determinístico (Dijkstra).

A desempate de empates usa sempre o identificador do roteador, o que
garante que a mesma rede produza a mesma tabela de roteamento em qualquer
execução, independentemente da ordem de inserção dos links.
"""

from __future__ import annotations

import heapq

from .network import Network

def dijkstra(network: Network, origem: str) -> dict[str, int]:
    """Calcula a distância mínima de origem a cada roteador alcançável.

    Returns:
        dict mapeando id do roteador -> distância mínima. Roteadores
        inalcançáveis não aparecem no resultado. A distância da origem até
        ela mesma é 0.

    Raises:
        KeyError: se origem não estiver na rede.
    """
    if origem not in network.roteadores:
        raise KeyError(f"roteador desconhecido: {origem}")

    distancias: dict[str, int] = {origem: 0}
    fila: list[tuple[int, str]] = [(0, origem)]
    visitados: set[str] = set()

    while fila:
        dist_atual, atual = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)

        for vizinho, custo in network.vizinhos(atual):
            if vizinho in visitados:
                continue
            nova_dist = dist_atual + custo
            if vizinho not in distancias or nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias
