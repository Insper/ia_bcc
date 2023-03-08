# Continuação: menor caminho entre duas cidades

Considerando o problema apresentado [na aula passada](../08_heuristica/index.md) e o código disponível em [src/Map2023.py](./src/Map2023.py) faça os seguintes testes abaixo. 

## Usando busca em profundidade iterativo

* **Encontrar um caminho entre a cidade *i* e *o*.**

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução? 
* A árvore de busca gerada é "inteligente"? 
* A solução encontrada é ótima? 

* **Encontre um caminho entre a cidade *b* e *o*.** 

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução? 
* A árvore de busca gerada é "inteligente"? 
* A solução encontrada é ótima?

## Usando busca de custo uniforme

Utilize o algoritmo de custo uniforme para encontrar uma solução para os problemas abaixo:

* da cidade i para a cidade o
* da cidade b para a cidade o
* da cidade i para a cidade x

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução?
* A árvore de busca gerada é "inteligente"?
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

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução?
* A árvore de busca gerada é "inteligente"?
* A solução encontrada é ótima?


## Usando busca A* 

E o algoritmo A-Estrela? 