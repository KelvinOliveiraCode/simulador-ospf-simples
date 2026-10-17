# BRIEF — simulador-ospf-simples

## Entregas

Projeto "simulador-ospf-simples" (área Redes): simulador OSPF simplificado com tabela de roteamento, em Python, sem dependências externas (biblioteca padrão, Python >= 3.10).

Arquivos criados:

- pyproject.toml — metadados, entry point `ospf-simulador`, pythonpath para `src/`, caminhos de teste do pytest.
- src/simulador_ospf_simples/__init__.py — pacote público (Router, Link, Network, RouteEntry, compute_routing_tables, dijkstra).
- src/simulador_ospf_simples/network.py — modelo de rede: roteadores, links bidirecionais com custo, vizinhos ordenados por id, menor custo em links paralelos.
- src/simulador_ospf_simples/dijkstra.py — Dijkstra determinístico: desempate de caminhos iguais pelo identificador do roteador; mesma rede = mesma tabela sempre.
- src/simulador_ospf_simples/routing.py — tabela de roteamento por roteador (destino, próximo salto, custo total); salto direto só quando é o caminho de menor custo.
- src/simulador_ospf_simples/__main__.py — CLI de demonstração com rede pré-configurada (R1–R2–R3–R4, salto 1, link direto R1–R4 custo 10).
- tests/conftest.py — fixtures: rede em linha com link direto caro; rede isolada (destino inalcançável).
- tests/test_network.py — roteadores, validação de link, custo negativo, link próprio, vizinhos ordenados.
- tests/test_dijkstra.py — distância zero na origem, custo direto, caminho multi-salto, caminho mais barato que o direto, inalcançável, origem desconhecida.
- tests/test_routing_table.py — tabela de roteamento esperada (crítico de aceitação), roteador sem links, destino inalcançável sem entrada, determinismo independente da ordem de inserção dos links.
- README.md — documentação bilíngue PT-BR + EN (descrição, como usar, testes, licença MIT, autor Kelvin Oliveira).
- LICENSE — texto da licença MIT.
- BRIEF.md — este arquivo.

## Como verificar

Na raiz do projeto (`C:\Users\Kelvin\AppData\Local\Temp\opencode\github-staging\projects\simulador-ospf-simples\`):

python -m pytest -q

Resultado esperado: 15 testes aprovados, 0 falhas, saída limpa (sem avisos ou erros).

Critério de aceitação coberto: `tests/test_routing_table.py::test_tabela_roteamento_esperada` compara a tabela gerada com a tabela esperada roteador por roteador (destino, próximo salto e custo total).

Demonstração:

$env:PYTHONPATH="src"; python -m simulador_ospf_simples

Validador: o workflow manager (eu).
