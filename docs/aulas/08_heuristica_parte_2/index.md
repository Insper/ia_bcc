# Continuação: menor caminho entre duas cidades

## Usando busca em profundidade iterativo

**Encontrar um caminho entre a cidade *i* e *o*.**

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução? 
* Quantos nodos o algoritmo de busca abriu até encontrar a solução? 
* A solução encontrada é ótima? 

**Encontre um caminho entre a cidade *b* e *o*.** 

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução? 
* Quantos nodos o algoritmo de busca abriu até encontrar a solução? 
* A solução encontrada é ótima?

## Usando busca de custo uniforme

Utilize o algoritmo de custo uniforme para encontrar uma solução para os problemas abaixo:

* da cidade i para a cidade o
* da cidade b para a cidade o
* da cidade i para a cidade x

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução?
* Quantos nodos o algoritmo de busca abriu até encontrar a solução?
* A solução encontrada é ótima?

## Usando busca gananciosa

Considerar o slide 32 em diante: 

<embed src="../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf" type="application/pdf" width="600" height="300">

* Que heurística podemos utilizar para este problema? Crie uma heurística e utilize o algoritmo `from aigyminsper.search.SearchAlgorithms import BuscaGananciosa` para encontrar as soluções para: 

* da cidade i para a cidade o
* da cidade b para a cidade o
* da cidade i para a cidade x

O algoritmo de busca `BuscaGananciosa` precisa de um método que define a heurística. Este método na implementação do pacote `aigyminsper` é definido como: 

```python
def h(self):
    return <<valor numérico>>
```

Para esta parte do exercício considere também o arquivo CSV com a definição das heurísticas: [MapHeuristicas.csv](./data/MapHeuristics.csv).

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução?
* Quantos nodos o algoritmo de busca abriu até encontrar a solução?
* A solução encontrada é ótima?


## Usando busca A* 

E o algoritmo A-Estrela? 


## Comparando algoritmos

Execute todos os objetivos listados abaixo para os algoritmos de busca também listados na tabela abaixo. 

|Objetivo | Algoritmo | Solução | Tempo de processamento|
|:--------|:----------|:---------:|:----------------------:|
| i $\rightarrow$ o | Custo Uniforme | | |
| b $\rightarrow$ o | Custo Uniforme | | |
| i $\rightarrow$ x | Custo Uniforme | | | 
| i $\rightarrow$ o | Ganancioso | | |
| b $\rightarrow$ o | Ganancioso | | |
| i $\rightarrow$ x | Ganancioso | | | 
| i $\rightarrow$ o | A-Estrela | | |
| b $\rightarrow$ o | A-Estrela | | |
| i $\rightarrow$ x | A-Estrela | | |
| i $\rightarrow$ o | A-Estrela ($h(N) = h(N) * 100) | | |
| b $\rightarrow$ o | A-Estrela ($h(N) = h(N) * 100)| | |
| i $\rightarrow$ x | A-Estrela ($h(N) = h(N) * 100)| | | 
| i $\rightarrow$ o | A-Estrela ($h(N) == 1$) | | |
| b $\rightarrow$ o | A-Estrela ($h(N) == 1$)| | | 
| i $\rightarrow$ x | A-Estrela ($h(N) == 1$)| | |

Anote na tabela acima o tempo de processamento e a solução encontrada e discuta os resultados obtidos:

* Qual foi o tempo de processamento até a implementação encontrar uma solução?
* Por que o tempo de processamento foi diferente para cada algoritmo?
* Por que a solução encontrada foi diferente em cada algoritmo?
* Por que a solução encontrada foi diferente em cada versão do A-Estrela? 

## Entrega

Este exercício é individual.

Crie um documento pdf com a tabela preenchida e com a resposta para as perguntas e envie via **blackboard**. A data limite para entrega é **10/09/2021**.
