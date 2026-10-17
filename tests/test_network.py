"""Testes do modelo de rede (roteadores e links com custo)."""

from __future__ import annotations

import pytest

from simulador_ospf_simples import Link, Network, Router


def test_adicionar_e_listar_roteadores() -> None:
    rede = Network()
    rede.adicionar_roteador(Router(id="R1", nome="Roteador 1"))
    rede.adicionar_roteador(Router(id="R2", nome="Roteador 2"))

    ids = sorted(rede.roteadores)
    assert ids == ["R1", "R2"]
    assert rede.roteadores["R1"].nome == "Roteador 1"


def test_adicionar_link_roteador_desconhecido_erro() -> None:
    rede = Network()
    rede.adicionar_roteador(Router(id="R1"))

    with pytest.raises(KeyError, match="roteador desconhecido: R9"):
        rede.adicionar_link(Link(origem="R1", destino="R9", custo=1))


def test_link_custo_negativo_rejeitado() -> None:
    with pytest.raises(ValueError, match="custo do link não pode ser negativo"):
        Link(origem="R1", destino="R2", custo=-1)


def test_link_para_si_mesmo_rejeitado() -> None:
    with pytest.raises(ValueError, match="não pode ligar o roteador a si mesmo"):
        Link(origem="R1", destino="R1", custo=1)


def test_vizinhos_ordenados_por_id_e_menor_custo(rede_linha: Network) -> None:
    vizinhos = rede_linha.vizinhos("R1")
    assert vizinhos == [("R2", 1), ("R4", 10)]
