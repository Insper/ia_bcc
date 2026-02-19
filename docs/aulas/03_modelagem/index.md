# Modelando problemas como um espaço de estados

Na [última aula](../02_agentes_autonomos/index.md) vimos o que é um agente autônomo e como ele pode perceber o ambiente e agir sobre ele. Ao final da aula, vimos um exemplo de um agente aspirador de pó e um grid world simples. Para resolver esses problemas, precisamos de uma forma de representar o estado do mundo, as ações que o agente pode executar e as transições entre os estados. Nesta aula, vamos continuar explorando esses conceitos e aprender a modelar problemas como um espaço de estados. Além disso, vamos começar a pensar em algoritmos de busca para encontrar soluções para esses problemas.


## Mais um grid world simples

Considere o ambiente representado abaixo, onde um agente pode se mover em quatro direções (cima, baixo, esquerda, direita) em um grid 3x3. O objetivo do agente é alcançar a célula marcada com "G" (goal). As células marcadas com as letras de "A" até "F" são células onde o agente pode estar, incluindo a célula marcada com "G". As células marcadas com "X" são obstáculos que o agente não pode atravessar.

```
+---+---+---+
| A | B | X |
+---+---+---+
| C | D | E |
+---+---+---+
| X | F | G |
+---+---+---+
```

Individualmente, responda as seguintes perguntas:

* Quais são os estados possíveis do mundo? 
* Quais são as ações que o agente pode executar?
* Quais são as consequências das ações sobre os estados? As ações são determinísticas?
* Qual é o estado inicial e qual é o estado final?
* Desenhe o grafo com todos os estados e transições para este problema.

## Procurando por soluções: algoritmos de busca

Dado um estado qualquer do mundo, como o agente pode encontrar uma sequência de ações que o leve ao estado final? Para isso, precisamos de um algoritmo de busca. Existem vários algoritmos de busca, como busca em largura, busca em profundidade, busca A*, entre outros. Cada um desses algoritmos tem suas próprias características e é adequado para diferentes tipos de problemas.

O objetivo desta aula é introduzir o conceito de algoritmo de busca, mais especificamente, usando os algoritmo de busca em largura e o algortimo de busca em profundidade.

## Material de referência

<embed src="../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf" type="application/pdf" width="600" height="300">