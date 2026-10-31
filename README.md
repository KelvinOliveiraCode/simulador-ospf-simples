# simulador-ospf-simples

[English](README.en.md) · **Português (Brasil)**

[![Python 3](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#) [![pytest](https://img.shields.io/badge/pytest-15%20testes-0A9EDC?style=flat-square&logo=pytest)](#) [![MIT License](https://img.shields.io/badge/License-MIT-f4c430?style=flat-square)](LICENSE)

## O que é

**Simulador de roteamento OSPF simplificado**: constrói uma topologia de rede (roteadores + enlaces com custo), executa o **algoritmo de Dijkstra** para calcular as rotas de menor custo e gera as **tabelas de roteamento** de cada roteador. É um laboratório educacional de redes em Python puro (stdlib).

## Status

Laboratório educacional funcional e testado (15 testes).

## Funcionalidades

- **Modelo** (`network.py`): `Router`, `Link` (origem, destino, custo), `Network` (adição de roteadores/enlaces).
- **Dijkstra** (`dijkstra.py`): caminho mais curto a partir de uma origem.
- **Tabela de roteamento** (`routing.py`): `compute_routing_tables` monta a tabela de cada roteador com next-hop e custo.
- **CLI**: `ospf-simulador` (demo com rede de exemplo R1-R4).

## Arquitetura

Pacote `simulador_ospf_simples` com três módulos: `network` (modelo), `dijkstra` (algoritmo), `routing` (tabelas).

## Stack

- Python ≥ 3.10, stdlib apenas
- pytest (dev)

## Estrutura do repositório

```
simulador-ospf-simples/
├── pyproject.toml · BRIEF.md
├── src/simulador_ospf_simples/
│   ├── network.py    # modelo de rede
│   ├── dijkstra.py   # algoritmo SPF
│   └── routing.py    # tabelas de roteamento
├── tests/            # 15 testes
└── LICENSE           # MIT
```

## Pré-requisitos e instalação

```bash
pip install -e .
```

## Como executar

```bash
ospf-simulador
# imprime as tabelas de roteamento da rede de exemplo (R1-R4)
```

## Testes e qualidade

```bash
PYTHONPATH=src python -m pytest tests/
# 15 passed
```

## Decisões técnicas e trade-offs

- Dijkstra sobre modelo de objetos: claro e didático; sem otimizações de performance para grades grandes.
- Stdlib: sem dependências; em troca, sem parser YAML embutido (para topologia real, instale PyYAML).

## Limitações conhecidas

- OSPF simplificado: sem áreas, sem LSA flooding, sem eleição de DR/BDR.
- A topologia de exemplo usa dicionário Python (não YAML externo) — adaptar para arquivo exigiria PyYAML.

## Processo de desenvolvimento

Projeto individual de Kelvin Oliveira, construído com agentes de IA orquestrados e revisado pelo autor. O algoritmo SPF e a revisão são do autor.

## Licença e autor

MIT — Copyright (c) 2026 Kelvin Rebelo de Oliveira. Autor: [Kelvin Oliveira](https://github.com/KelvinOliveiraCode) · [Portfólio](https://kelvinoliveiracode.github.io/portfolio/)
