# Continuação sobre modelagem

O objetivo da aula de hoje é implementar agentes capazes de resolver os problemas abaixo. 

## O homem, o lobo, o carneiro e o cesto de alface

Uma pessoa, um lobo, um carneiro e um cesto de alface estão à beira de
  um rio. Dispondo de um barco no qual pode carregar apenas um dos
  outros três, a pessoa deve transportar tudo para a outra margem.
  Determine uma série de travessias que respeite a seguinte condição:
  em nenhum momento devem ser deixados juntos e sozinhos o lobo e o
  carneiro ou o carneiro e o cesto de alface.

## Banda U2

A banda U2 tem um concerto que começa daqui a 17 minutos e
  todos precisam cruzar uma ponte par chegar lá. Todos os 4
  participantes estão do mesmo lado da ponte. É noite. Só
  há uma lanterna. A ponte suporta, no máximo, duas
  pessoas. Qualquer pessoa que passe, uma ou duas, deve passar com a
  lanterna na mão. A lanterna deve ser levada de um lado para outro
  e não ser jogada. Cada membro da banda tem um tempo diferente
  para passar de um lado para o outro. O par deve andar no tempo do
  menos veloz: Bono: 1 minuto para passar; Edge: 2 minutos para
  passar; Adam: 5 minutos para passar; e Larry: 10 minutos para
  passar.

O problema consiste em ter os quatro elementos da banda do outro lado
da ponte no menor tempo possível.

??? warning "Tem algo dirente neste problema..." 
    O que é diferente neste problema em relação aos outros?


<!--

## Cavalo e tabuleiro de xadrez

Considerando um tabuleiro de xadrez (`8x8`) com um
  único cavalo, quais os movimentos que o cavalo deve fazer para
  percorrer todas as posições do tabuleiro uma única vez e
  retornar ao ponto de partida?

## As 8 rainhas

Coloque oito rainhas em um tabuleiro de
  xadrez (`8x8` casas) de maneira que nenhuma rainha ameace
  outra, i.e., as rainhas não devem compartilhar colunas, linhas ou
  diagonais do tabuleiro.

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

-->