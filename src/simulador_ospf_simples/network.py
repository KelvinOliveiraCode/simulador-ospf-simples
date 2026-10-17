"""Modelo de rede: roteadores e links com custo."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Router:
    """Roteador da rede.

    Attributes:
        id: identificador único do roteador (ex.: "R1").
        nome: nome legível para exibição.
    """

    id: str
    nome: str = ""


@dataclass(frozen=True, order=True)
class Link:
    """Link bidirecional entre dois roteadores com custo não-negativo."""

    origem: str
    destino: str
    custo: int

    def __post_init__(self) -> None:
        if self.custo < 0:
            raise ValueError(f"custo do link não pode ser negativo: {self.custo}")
        if self.origem == self.destino:
            raise ValueError(
                f"link não pode ligar o roteador a si mesmo: {self.origem}"
            )


class Network:
    """Rede de roteadores interligados por links com custo."""

    def __init__(self) -> None:
        self._roteadores: dict[str, Router] = {}
        self._links: list[Link] = []

    def adicionar_roteador(self, roteador: Router) -> None:
        """Registra um roteador na rede."""
        self._roteadores[roteador.id] = roteador

    def adicionar_link(self, link: Link) -> None:
        """Registra um link bidirecional na rede.

        Raises:
            KeyError: se origem ou destino não estiverem na rede.
        """
        if link.origem not in self._roteadores:
            raise KeyError(f"roteador desconhecido: {link.origem}")
        if link.destino not in self._roteadores:
            raise KeyError(f"roteador desconhecido: {link.destino}")
        self._links.append(link)

    @property
    def roteadores(self) -> dict[str, Router]:
        return dict(self._roteadores)

    @property
    def links(self) -> list[Link]:
        return list(self._links)

    def vizinhos(self, roteador_id: str) -> list[tuple[str, int]]:
        """Retorna [(id_vizinho, custo)] de um roteador, ordenado por id."""
        if roteador_id not in self._roteadores:
            raise KeyError(f"roteador desconhecido: {roteador_id}")
        resultado: dict[str, int] = {}
        for link in self._links:
            if link.origem == roteador_id:
                alvo = link.destino
            elif link.destino == roteador_id:
                alvo = link.origem
            else:
                continue
            # Em caso de links paralelos, fica com o menor custo.
            if alvo not in resultado or link.custo < resultado[alvo]:
                resultado[alvo] = link.custo
        return sorted(resultado.items())

    def custo_link(self, origem: str, destino: str) -> int | None:
        """Custo do link direto entre origem e destino, ou None se inexistente."""
        for link in self._links:
            if {link.origem, link.destino} == {origem, destino}:
                return link.custo
        return None
