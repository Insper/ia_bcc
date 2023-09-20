# Continuação: menor caminho entre duas cidades

Considerando o problema apresentado [na aula passada](../08_heuristica/index.md) e o código disponível em [src/Map2023.py](./src/Map2023.py) faça os seguintes testes abaixo. 

Considere também o arquivo CSV com a definição das heurísticas: [MapHeuristicas.csv](./data/MapHeuristics.csv).

## Usando busca em profundidade iterativo

**Encontrar um caminho entre a cidade *i* e *o*.**

Perguntas:

* Qual foi o tempo de processamento até a implementação encontrar uma solução? 
* A árvore de busca gerada é "inteligente"? 
* A solução encontrada é ótima? 

**Encontre um caminho entre a cidade *b* e *o*.** 

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

Crie um documento pdf e envie via blackboard. A data limite para entrega é **23/09/2021**.

## Código do problema do Mapa

```python
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.SearchAlgorithms import BuscaGananciosa
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State
import time
import networkx as nx
import csv

class Map(State):

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def successors(self):
        sucessors = []
        neighbors = Map.area[self.city]
        for next_city in neighbors:
            sucessors.append(Map(next_city[1], next_city[0], next_city[1], self.goal))
        return sucessors
    
    def is_goal(self):
        return (self.city == self.goal)
    
    def description(self):
        return "Um mapa para procurar"
    
    def cost(self):
        return self.cost_value
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return self.city
    
    def h(self):
        return int(Map.g.edges[self.city,self.goal]['distance'])
        #return random.randint(1,10)
        #return 1

    @staticmethod
    def createArea():
        Map.area = {
            'a':[(3,'b'),(6,'c')],
            'b':[(3,'a'),(3,'h'),(3,'k')],
            'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
            'd':[(3,'c'),(1,'f'),(1,'e')],
            'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
            'f':[(1,'g'),(1,'e'),(1,'d')],
            'g':[(2,'c'),(1,'f'),(2,'h')],
            'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
            'i':[(2,'e'),(2,'h')],
            'l':[(1,'k')],
            'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
            'm':[(2,'n'),(1,'x'),(14,'e')],
            'n':[(2,'m'),(3,'k')],
            'o':[(2,'c')],
            'p':[(2,'c')],
            'x':[(1,'m')]
            }
        
    @staticmethod
    def createHeuristics():
        #
        # O arquvo MapHeuristics.csv considera apenas os objetivos "o" e "x"
        # TODO modificar o arquivo para considerar todas as cidades. talvez modificar
        # a estrutura do arquivo considerando uma estrutura otimizada
        #
        Map.g = nx.Graph()
        f = csv.reader(open("data/MapHeuristics.csv","r"))
        for row in f: 
            Map.g.add_edge(row[0],row[1], distance = row[2])

def main():

    Map.createArea()
    Map.createHeuristics()

    #state = Map('i', 0, 'i', 'o')
    state = Map('b', 0, 'b', 'o')
    #state = Map('i', 0, 'i', 'x')
    #algorithm = BuscaLargura()
    #algorithm = BuscaCustoUniforme()
    algorithm = BuscaGananciosa()
    ts = time.time()
    result = algorithm.search(state, trace=True)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))

if __name__ == '__main__':
    main()
```

??? note "Atenção!"
    Uma nova versão da biblioteca foi disponibilizada. Para atualizar a biblioteca, execute o comando abaixo no terminal: 

    ```bash
    pip install --upgrade aigyminsper
    ```

    Esta nova versão possui a possibilidade de poda da árvore de busca pelo método de busca. 

