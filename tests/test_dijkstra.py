"""Testes do algoritmo Dijkstra determinístico."""

from __future__ import annotations

import pytest

from simulador_ospf_simples.dijkstra import dijkstra


def test_distancia_origem_e_zero(rede_linha) -> None:
    distancias = dijkstra(rede_linha, "R1")
    assert distancias["R1"] == 0


def test_caminho_direto_soma_custo_do_link(rede_linha) -> None:
    distancias = dijkstra(rede_linha, "R1")
    assert distancias["R2"] == 1


def test_caminho_multiplo_soma_custos(rede_linha) -> None:
    distancias = dijkstra(rede_linha, "R1")
    assert distancias["R3"] == 2  # R1 -> R2 -> R3


def test_escolhe_caminho_mais_barato_e_nao_o_direto_caro(rede_linha) -> None:
    distancias = dijkstra(rede_linha, "R1")
    assert distancias["R4"] == 3  # R1->R2->R3->R4 custa 3, link direto custa 10


def test_roteador_inalcanzavel_nao_aparece(rede_isolada) -> None:
    distancias = dijkstra(rede_isolada, "R1")
    assert "R2" not in distancias


def test_origem_desconhecida_erro(rede_linha) -> None:
    with pytest.raises(KeyError, match="roteador desconhecido: R9"):
        dijkstra(rede_linha, "R9")
