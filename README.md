# simulador-ospf-simples

## Português

### Descrição

simulador-ospf-simples é um simulador de roteamento OSPF simplificado escrito em Python. Você monta uma rede com roteadores e links bidirecionais, cada link com custo inteiro não-negativo, e o programa calcula a tabela de roteamento de cada roteador com o algoritmo de Dijkstra. Caminhos de custo igual são desempatados pelo identificador do roteador, então a mesma rede gera sempre a mesma tabela.

Não tem dependências externas: roda apenas com a biblioteca padrão do Python (>= 3.10).

### Como usar

Na raiz do projeto:

$env:PYTHONPATH="src"; python -m simulador_ospf_simples

Saída da rede pré-configurada (R1–R2–R3–R4 com salto de custo 1, mais link direto R1–R4 de custo 10):

Tabela de roteamento de R1:
  destino  proximo_salto  custo
  R2       R2             1
  R3       R2             2
  R4       R2             3

Tabela de roteamento de R2:
  destino  proximo_salto  custo
  R1       R1             1
  R3       R3             1
  R4       R3             2

Tabela de roteamento de R3:
  destino  proximo_salto  custo
  R1       R2             2
  R2       R2             1
  R4       R4             1

Tabela de roteamento de R4:
  destino  proximo_salto  custo
  R1       R3             3
  R2       R3             2
  R3       R3             1

R4 chega a R1 por R3, custo 3 — não pelo link direto de custo 10. O algoritmo escolhe o caminho de menor custo acumulado, não o link direto.

Para usar com sua própria rede:

from simulador_ospf_simples import Link, Network, Router, compute_routing_tables

rede = Network()
rede.adicionar_roteador(Router(id="R1"))
rede.adicionar_roteador(Router(id="R2"))
rede.adicionar_link(Link(origem="R1", destino="R2", custo=5))

tabelas = compute_routing_tables(rede)

### Testes

O projeto usa pytest. Na raiz do projeto:

python -m pytest -q

Esperado: 15 testes aprovados, sem falhas, incluindo o teste de tabela de roteamento esperada em tests/test_routing_table.py::test_tabela_roteamento_esperada.

### Licença

MIT License. Veja o arquivo LICENSE.

### Autor

Kelvin Oliveira

## English

### Description

simulador-ospf-simples is a simplified OSPF routing simulator written in Python. You build a network with routers and bidirectional links, each link with a non-negative integer cost, and the program computes the routing table of each router using Dijkstra's algorithm. Equal-cost paths are broken by router identifier, so the same network always produces the same table.

No external dependencies: it runs on the Python standard library only (>= 3.10).

### How to use

In the project root:

$env:PYTHONPATH="src"; python -m simulador_ospf_simples

Output of the built-in network (R1–R2–R3–R4 with hop cost 1, plus direct link R1–R4 of cost 10):

Routing table of R1:
  destination  next_hop  cost
  R2           R2        1
  R3           R2        2
  R4           R2        3

Routing table of R2:
  destination  next_hop  cost
  R1           R1        1
  R3           R3        1
  R4           R3        2

Routing table of R3:
  destination  next_hop  cost
  R1           R2        2
  R2           R2        1
  R4           R4        1

Routing table of R4:
  destination  next_hop  cost
  R1           R3        3
  R2           R3        2
  R3           R3        1

R4 reaches R1 via R3 at cost 3 — not via the direct link of cost 10. The algorithm picks the lowest accumulated cost, not the direct link.

To use with your own network:

from simulador_ospf_simples import Link, Network, Router, compute_routing_tables

rede = Network()
rede.adicionar_roteador(Router(id="R1"))
rede.adicionar_roteador(Router(id="R2"))
rede.adicionar_link(Link(origem="R1", destino="R2", custo=5))

tabelas = compute_routing_tables(rede)

### Tests

The project uses pytest. In the project root:

python -m pytest -q

Expected: 15 tests pass, no failures, including the expected routing table test at tests/test_routing_table.py::test_tabela_roteamento_esperada.

### License

MIT License. See the LICENSE file.

### Author

Kelvin Oliveira
