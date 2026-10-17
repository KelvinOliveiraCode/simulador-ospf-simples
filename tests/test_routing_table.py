"""Testes da tabela de roteamento gerada por roteador (critério de aceitação)."""

from __future__ import annotations

import pytest

from simulador_ospf_simples import Link, Network, Router
from simulador_ospf_simples.routing import RouteEntry, compute_routing_tables


def rede_outra_ordem() -> Network:
    """Mesma rede da fixture, links inseridos em ordem diferente."""

    rede = Network()
    for rid in ("R4", "R3", "R2", "R1"):
        rede.adicionar_roteador(Router(id=rid))
    for origem, destino, custo in (
        ("R1", "R4", 10),
        ("R3", "R4", 1),
        ("R2", "R3", 1),
        ("R1", "R2", 1),
    ):
        rede.adicionar_link(Link(origem=origem, destino=destino, custo=custo))
    return rede


def tabela_esperada() -> dict[str, dict[str, RouteEntry]]:
    return {
        "R1": {
            "R2": RouteEntry(destino="R2", proximo_salto="R2", custo_total=1),
            "R3": RouteEntry(destino="R3", proximo_salto="R2", custo_total=2),
            "R4": RouteEntry(destino="R4", proximo_salto="R2", custo_total=3),
        },
        "R2": {
            "R1": RouteEntry(destino="R1", proximo_salto="R1", custo_total=1),
            "R3": RouteEntry(destino="R3", proximo_salto="R3", custo_total=1),
            "R4": RouteEntry(destino="R4", proximo_salto="R3", custo_total=2),
        },
        "R3": {
            "R1": RouteEntry(destino="R1", proximo_salto="R2", custo_total=2),
            "R2": RouteEntry(destino="R2", proximo_salto="R2", custo_total=1),
            "R4": RouteEntry(destino="R4", proximo_salto="R4", custo_total=1),
        },
        "R4": {
            "R1": RouteEntry(destino="R1", proximo_salto="R3", custo_total=3),
            "R2": RouteEntry(destino="R2", proximo_salto="R3", custo_total=2),
            "R3": RouteEntry(destino="R3", proximo_salto="R3", custo_total=1),
        },
    }


def test_tabela_roteamento_esperada(rede_linha) -> None:
    """Critério de aceitação: tabela correta para a rede de exemplo."""

    tabelas = compute_routing_tables(rede_linha)
    assert tabelas == tabela_esperada()


def test_roteador_sem_links_tabela_vazia(rede_isolada) -> None:
    tabelas = compute_routing_tables(rede_isolada)
    assert tabelas == {"R1": {}, "R2": {}}


def test_destino_inalcanzavel_sem_entrada(rede_isolada) -> None:
    tabelas = compute_routing_tables(rede_isolada)
    assert "R2" not in tabelas["R1"]
    assert "R1" not in tabelas["R2"]


def test_tabelas_sao_deterministicas_independente_da_ordem_de_insercao(
    rede_linha,
) -> None:
    tabelas_padrao = compute_routing_tables(rede_linha)
    tabelas_outra = compute_routing_tables(rede_outra_ordem())
    assert tabelas_padrao == tabelas_outra
