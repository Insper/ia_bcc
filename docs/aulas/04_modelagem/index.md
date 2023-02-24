# Modelagem dos problemas

Na aula passada começamos a implementar um agente que limpa casas com $2$ quartos. Para tanto, utilizamos uma biblioteca que já implementa alguns algoritmos de busca. 

Para instalar esta biblioteca basta digitar: 

```bash
pip install aigyminsper
```

Uma solução possível encontrada para implementar o agente limpador de quartos em uma casa de 2 quartos foi: 

```python
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class AspiradorPo(State):

    def __init__(self, op, posicao, s_esq, s_dir):
        self.operator = op
        # DIR; ESQ
        self.posicao_robo = posicao
        # LIMPO; SUJO
        self.situacao_esq = s_esq
        # LIMPO; SUJO
        self.situacao_dir = s_dir
    
    def sucessors(self):
        sucessors = []
        # esq
        sucessors.append(AspiradorPo("esq","ESQ",self.situacao_esq,self.situacao_dir))
        # dir
        sucessors.append(AspiradorPo("dir","DIR",self.situacao_esq,self.situacao_dir))
        # limpar
        if self.posicao_robo == 'ESQ':
            sucessors.append(AspiradorPo("limpar",self.posicao_robo,'LIMPO',self.situacao_dir))
        else:
            sucessors.append(AspiradorPo('limpar',self.posicao_robo,self.situacao_esq,'LIMPO'))
        
        return sucessors
    
    def is_goal(self):
        if (self.situacao_dir == 'LIMPO') and (self.situacao_esq == 'LIMPO') and (self.posicao_robo == "ESQ"):
            return True
        return False 

    def cost(self):
        return 1

    def description(self):
        return "Implementa um aspirador de po para 2 quartos"

    def env(self):
        return self.operator


def main():
    state = AspiradorPo('','ESQ','SUJO','SUJO')
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

**Questões**:

* O que significa `algorithm = BuscaLargura()`? 
* Será que é possível utilizar outros algoritmos? 

## Exercício 2: Aspirador de Pó com $4$ quartos.

Vamos implementar um aspirador de pó que atua em um ambiente com 4 quartos? Um quadrado $2 \times 2$?

Mas, antes de implementar usando uma estrutura similar a descrita acima, responda as questões abaixo: 

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

## Exercício 3: Aspirador de Pó em um mapa $10 \times 10$ e com algumas ações diferentes.

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

## Vamos entender as diferenças entre os algoritmos de busca? 

Se você já terminou as implementações acima, então leia o material neste [link](../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf). Em especial, do primeiro ao slide de número 28. 
