"""Fixtures compartilhadas pelos testes do simulador OSPF."""

from __future__ import annotations

import pytest

from simulador_ospf_simples import Link, Network, Router


@pytest.fixture
def rede_linha() -> Network:
    """Rede em linha: R1--1--R2--1--R3--1--R4 com link direto R1--10--R4."""

    rede = Network()
    for rid in ("R1", "R2", "R3", "R4"):
        rede.adicionar_roteador(Router(id=rid))
    for origem, destino, custo in (
        ("R1", "R2", 1),
        ("R2", "R3", 1),
        ("R3", "R4", 1),
        ("R1", "R4", 10),
    ):
        rede.adicionar_link(Link(origem=origem, destino=destino, custo=custo))
    return rede


@pytest.fixture
def rede_isolada() -> Network:
    """Dois roteadores sem link entre si."""

    rede = Network()
    rede.adicionar_roteador(Router(id="R1"))
    rede.adicionar_roteador(Router(id="R2"))
    return rede
