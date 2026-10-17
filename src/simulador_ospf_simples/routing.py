"""Geração de tabela de roteamento por roteador.

Para cada roteador de origem, executa Dijkstra e monta uma entrada de
roteamento por destino alcançável. O próximo salto é o vizinho direto que
inicia o caminho mínimo; em camamentos de custo igual, escolhe-se o vizinho
de identificador menor, o que torna a tabela totalmente determinística.
"""

from __future__ import annotations

from dataclasses import dataclass

from .dijkstra import dijkstra
from .network import Network


@dataclass(frozen=True, order=True)
class RouteEntry:
    """Uma linha da tabela de roteamento de um roteador.

    Attributes:
        destino: id do roteador de destino.
        proximo_salto: id do primeiro roteador no caminho até o destino
            (o próprio destino para links diretos; ``None`` para a origem).
        custo_total: custo acumulado do caminho mínimo.
    """

    destino: str
    proximo_salto: str | None
    custo_total: int


def compute_routing_tables(network: Network) -> dict[str, dict[str, RouteEntry]]:
    """Calcula a tabela de roteamento de cada roteador da rede.

    Returns:
        dict {id_roteador: {id_destino: RouteEntry}}. A tabela de um
        roteador não contém entrada para ele mesmo nem para destinos
        inalcançáveis.

    Raises:
        KeyError: se a rede estiver vazia.
    """
    if not network.roteadores:
        return {}

    distancias_por_origem: dict[str, dict[str, int]] = {
        roteador.id: dijkstra(network, roteador.id)
        for roteador in network.roteadores.values()
    }

    tabelas: dict[str, dict[str, RouteEntry]] = {}
    for origem in network.roteadores:
        dist_origem: dict[str, int] = distancias_por_origem[origem]
        tabela: dict[str, RouteEntry] = {}
        for destino, custo_total in dist_origem.items():
            if destino == origem:
                continue
            proximo_salto = _escolher_proximo_salto(
                network, origem, destino, distancias_por_origem
            )
            tabela[destino] = RouteEntry(
                destino=destino,
                proximo_salto=proximo_salto,
                custo_total=custo_total,
            )
        tabelas[origem] = tabela

    return tabelas


def _escolher_proximo_salto(
    network: Network,
    origem: str,
    destino: str,
    distancias_por_origem: dict[str, dict[str, int]],
) -> str | None:
    """Escolhe o próximo salto determinístico para destino a partir de origem.

    Um vizinho é candidato quando passar por ele reproduz a distância mínima
    até o destino. Isso cobre tanto links diretos (quando são o caminho mais
    barato) quanto encaminhamento multi-salto. Entre candidatos de custo
    igual, vence o identificador menor — totalmente determinístico.
    """
    dist_destino = distancias_por_origem[origem][destino]
    candidatos: list[str] = []
    for vizinho, custo_link in network.vizinhos(origem):
        dist_vizinho = distancias_por_origem.get(vizinho, {})
        custo_via_vizinho = dist_vizinho.get(destino)
        if custo_via_vizinho is None:
            continue
        if custo_link + custo_via_vizinho == dist_destino:
            candidatos.append(vizinho)

    if not candidatos:
        return None
    return min(candidatos)
