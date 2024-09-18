# Jogador de jogo da velha


## Pré-atividade

Pense nas perguntas abaixo: 

1. O que é um ambiente competitivo de soma zero?
1. Qual o objetivo do algoritmo Min-Max? Em outras palavras, por que um agente autônomo que atua em um ambiente competitivo deve usar o algoritmo Min-Max?
1. O que é função de utilidade? Por que utilizar funções de utilidade? 
1. Qual é a relação da profundidade da árvore de busca do Min-Max com o desempenho final do agente? Existe correlação? Justifique a sua resposta.


## Objetivo da atividade

O objetivo desta atividade é implementar um jogador de jogo da velha usando o algoritmo Min-Max. 

O ambiente que vamos utilizar para implementar este jogador é o `kaggle-environments`. 

## Tutorial sobre o kaggle-environments

Para instalar o pacote execute o comando:

```bash
pip install kaggle-environments
```

O código fonte deste pacote e alguma documentação está disponível [neste link](https://github.com/Kaggle/kaggle-environments). 

Além disso, [neste link](tictactoe.ipynb) tem um tutorial bem básico sobre o funcionamento deste ambiente. Para aqueles que estão com dificuldade em instalar o pacote do kaggle, utilizem o [Google Colab](https://colab.research.google.com/gist/fbarth/ad7d167798a0d9097d2aca4a1c98c367/tictactoe.ipynb).

## Implementação para conceito C

* Implemente um agente usando o algoritmo `MinMax`, com limite de profundidade, capaz de jogar o jogo da velha.
* Utilize uma função de utilidade não muito complexa, mas que você acredita que é correta para o jogo da velha. No caso do jogo da velha, a profundidade pode variar de `1` até `9`. 
* Os resultados obtidos pelo seu agente não são importantes. 

Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`.

## Implementação para conceito B

* Para obter conceito B você deve fazer todos os itens especificados no conceito C. Mas, agora, você deve implementar uma função de utilidade mais complexa e que você acredita que é mais correta para o jogo da velha. 
* Neste caso, o seu agente não pode perder nenhum jogo.

Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`.

## Implementação para conceito A+

* Implemente um agente usando o algoritmo `MinMax` com **poda alpha-beta**, com limite de profundidade, capaz de jogar o jogo da velha.
* Você pode utilizar a mesma função de utilidade implementada anteriormente.
* Neste caso o seu agente não pode perder nenhum jogo e deve ganhar sempre que possível. Você deve perceber uma melhora no tempo de execução de cada jogada do seu agente.

* Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`.

## Entrega

* Para a implementação e entrega deste exercício nós vamos utilizar o Github Classroom. O link para para envio do projeto é este aqui [https://classroom.github.com/a/RrBlJCJA](https://classroom.github.com/a/RrBlJCJA). 

* A entrega é em equipes com até 3 integrantes e o  **prazo para a entrega** é 27/09/2024 (sexta-feira) até às 23:30 horas.


<!--
## Um possível solução para o problema

Uma possível solução para este problema está disponível [aqui](./tictactoe_minmax.ipynb).
-->