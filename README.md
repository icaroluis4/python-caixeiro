# Caixeiro Viajante
Este é um programa que implementa o algoritmo do Caixeiro Viajante em Python. O Caixeiro Viajante é um problema clássico de otimização que busca encontrar a rota mais curta para visitar um conjunto de cidades, passando por cada cidade uma única vez e retornando à cidade de origem.

O programa utiliza permutações para gerar todas as possíveis rotas entre as cidades fornecidas e calcula a distância total de cada rota. A distância entre as cidades é obtida através de um conjunto pré-definido de distâncias aproximadas.

## Funcionalidades
* Cálculo da distância entre duas cidades: A função calcular_distancia recebe duas cidades como parâmetros e retorna a distância entre elas. As distâncias são fornecidas anteriormente e armazenadas em um dicionário.

* Cálculo da distância total de uma rota: A função calcular_distancia_total recebe uma rota (uma lista de cidades) e o dicionário de distâncias como parâmetros. Ela calcula a distância total percorrida ao seguir essa rota, considerando as distâncias entre as cidades.

* Algoritmo do Caixeiro Viajante: A função caixeiro_viajante recebe uma lista de cidades como parâmetro. Ela gera todas as permutações possíveis das cidades, calcula a distância total para cada rota e encontra a rota com a menor distância total.
