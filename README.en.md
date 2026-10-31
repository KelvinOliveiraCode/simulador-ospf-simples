# simulador-ospf-simples

**English** · [Português (Brasil)](README.md)

[![Python 3](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#) [![pytest](https://img.shields.io/badge/pytest-15%20tests-0A9EDC?style=flat-square&logo=pytest)](#) [![MIT License](https://img.shields.io/badge/License-MIT-f4c430?style=flat-square)](LICENSE)

## What it is

A **simplified OSPF routing simulator**: it builds a network topology (routers + links with cost), runs **Dijkstra's algorithm** to compute the least-cost paths and generates each router's **routing table**. It is an educational networking lab in pure Python (stdlib).

## Status

An educational lab, working and tested (15 tests).

## Features

- **Model** (`network.py`): `Router`, `Link` (source, destination, cost), `Network` (add routers/links).
- **Dijkstra** (`dijkstra.py`): shortest path from a source.
- **Routing table** (`routing.py`): `compute_routing_tables` builds each router's table with next-hop and cost.
- **CLI**: `ospf-simulador` (demo with example R1-R4 network).

## Architecture

A `simulador_ospf_simples` package with three modules: `network` (model), `dijkstra` (algorithm), `routing` (tables).

## Stack

- Python ≥ 3.10, stdlib only
- pytest (dev)

## Repository layout

```
simulador-ospf-simples/
├── pyproject.toml · BRIEF.md
├── src/simulador_ospf_simples/
│   ├── network.py    # network model
│   ├── dijkstra.py   # SPF algorithm
│   └── routing.py    # routing tables
├── tests/            # 15 tests
└── LICENSE           # MIT
```

## Prerequisites and installation

```bash
pip install -e .
```

## How to run

```bash
ospf-simulador
# prints the routing tables of the example network (R1-R4)
```

## Tests and quality

```bash
PYTHONPATH=src python -m pytest tests/
# 15 passed
```

## Technical decisions and trade-offs

- Dijkstra on an object model: clear and didactic; no performance optimizations for large grids.
- Stdlib: zero dependencies; in exchange, no built-in YAML parser (add PyYAML for external files).

## Known limitations

- Simplified OSPF: no areas, no LSA flooding, no DR/BDR election.
- The example uses a Python dict (not an external YAML file) — adapting to file input requires PyYAML.

## Development process

An individual project by Kelvin Oliveira, built with orchestrated AI agents and reviewed by the author. The SPF algorithm and the review are the author's.

## License and author

MIT — Copyright (c) 2026 Kelvin Rebelo de Oliveira. Author: [Kelvin Oliveira](https://github.com/KelvinOliveiraCode) · [Portfolio](https://kelvinoliveiracode.github.io/portfolio/)
