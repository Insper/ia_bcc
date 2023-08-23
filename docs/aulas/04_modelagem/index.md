# Modelagem dos problemas

Na aula passada começamos a implementar um agente que limpa casas com $2$ quartos. Para tanto, utilizamos uma biblioteca que já implementa alguns algoritmos de busca. Uma solução possível para implementar o agente limpador de quartos em uma casa de 2 quartos é: 

```python
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class AspiradorPo(State):

    def __init__(self, op, quarto_esq, quarto_dir, robo):
        # You must use this name for the operator!
        self.operator = op
        self.quarto_esq = quarto_esq
        self.quarto_dir = quarto_dir
        self.robo = robo
    
    def successors(self):
        successors = []
        successors.append(AspiradorPo('esq',self.quarto_esq,self.quarto_dir,'esq'))
        successors.append(AspiradorPo('dir',self.quarto_esq,self.quarto_dir,'dir'))
        if self.robo == 'esq':
            successors.append(AspiradorPo("limpar","limpo",self.quarto_dir,self.robo))
        else:
            successors.append(AspiradorPo("limpar",self.quarto_esq,"limpo",self.robo))
        return successors
    
    def is_goal(self):
        return self.quarto_esq == 'limpo' and self.quarto_dir == 'limpo' and self.robo == 'esq'
    
    def description(self):
        return "Problema clássico do robô aspirador de pó com 2 quartos"
    
    def cost(self):
        return 1
    
    def env(self):
        return f'(robô no quarto {self.robo}, quarto da esquerda está {self.quarto_esq}, quarto da direita está {self.quarto_dir})'


def main():
    robo = input('Onde o robô está? (esq/dir) ')
    quarto_esq = input('Condição do quarto da esquerda? (limpo/sujo) ')
    quarto_dir = input('Condição do quarto da direita? (limpo/sujo) ')
    state = AspiradorPo('',quarto_esq,quarto_dir,robo)
    print('Aplicando o algoritmo de busca em largura')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
```

??? "Questão"
    
    O que significa `algorithm = BuscaLargura()`? 


## Comportamento do algoritmo de Busca em Largura

Na hora de chamar o método `search` altere o código de: 

```python
    algorithm = BuscaLargura()
    result = algorithm.search(state)
```

para: 

```python
    algorithm = BuscaLargura()
    result = algorithm.search(state, trace=True)
```

adicionando o parâmetro `trace=True`. Tente entender o que acontece.

## Aspirador de Pó em uma casa 10 por 10.

Neste exercício o agente sabe executar outras ações, mas o objetivo dele permanece o mesmo. As ações são: 

* ir para frente;
* virar para a esquerda;
* virar para a direita, e;
* limpar

E as dimensões da casa são de $10 \times 10$ quartos. 

* O que é relevante representar nos estados do mundo? Como os
    estados são estruturados (estrutura de dados) e qual o significado
    dela (dos campos)?
* Mostre como ficam representados os estados inicial e final
    segundo a representação adotada.
* Quais as operações sobre os estados?
    (detalhe como cada operação irá alterar os estados e quais as
    condições para cada operação ser executada)
* Qual a estimativa do tamanho do espaço de busca (número de
    estados possíveis)?
* Será que o algoritmo de busca em largura consegue encontrar resposta para todas as configurações iniciais? 


??? "Questão"
    
    Será que é possível utilizar outros algoritmos? 

## Próximas atividades

Se você já terminou as implementações acima e as implementações da [aula anterior](../03_configuracao/index.md), então leia o material neste [link](../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf). Em especial, do primeiro ao slide de número 28. 
