# Jogador de jogo da velha


<!--
## Pré-atividade

Responda as perguntas abaixo: 

1. O que é um ambiente competitivo de soma zero?
1. Qual o objetivo do algoritmo Min-Max? Em outras palavras, por que um agente autônomo que atua em um ambiente competitivo deve usar o algoritmo Min-Max?
1. O que é função de utilidade? Por que utilizar funções de utilidade? 
1. Qual é a relação da profundidade da árvore de busca do Min-Max com o desempenho final do agente? Existe correlação? Justifique a sua resposta.

-->

## Objetivo da atividade

O objetivo desta atividade é implementar um jogador de jogo da velha usando o algoritmo Min-Max e avaliar o impacto da 
profundidade no desempenho do agente. 

O ambiente que vamos utilizar para implementar este jogador é o `kaggle-environments`. 

## Tutorial sobre o kaggle-environments

Para instalar o pacote execute o comando:

```bash
pip install kaggle-environments
```

O código fonte deste pacote e alguma documentação está disponível [neste link](https://github.com/Kaggle/kaggle-environments). 

Além disso, [neste link](tictactoe.ipynb) tem um tutorial bem básico sobre o funcionamento deste ambiente. Para aqueles que estão com dificuldade em instalar o pacote do kaggle, utilizem o [Google Colab](https://colab.research.google.com/gist/fbarth/ad7d167798a0d9097d2aca4a1c98c367/tictactoe.ipynb).

## Implementação para conceito B

* Implemente um agente usando o algoritmo `MinMax`, com limite de profundidade, capaz de jogar o jogo da velha.
* Utilize uma função de utilidade não muito complexa, mas que você acredita que é correta para o jogo da velha.
* No caso do jogo da velha, a profundidade pode variar de `1` até `9`. 
* Para cada profundidade você deve executar `200` jogos do seu jogador contra o jogador `random`, onde `100` jogos o seu jogador é o primeiro a jogar e `100` jogos onde o seu jogador é o segundo a jogar. Ao final deste processo, você terá uma tabela parecida com esta: 

| Profundidade | Quantidade de vitórias | Quantidade de derrotas | Quantidade de empates | Tempo médio por jogada | Desvio padrão |
|--------------|------------------------|------------------------|------------------------|------------------------|---------------|
| 1            | 100                    | 100                    | 0                      | 0.1                    | 0.01          |
| 2            | 100                    | 100                    | 0                      | 0.2                    | 0.02          |

* Para cada jogada feita pelo seu jogador você deve medir quanto tempo ele gasta para tomar a decisão e calcular a média e o desvio padrão.
* Você deve encontrar uma forma gráfica para sumarizar os dados existentes na tabela acima. 

Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`.  

## Implementação para conceito A+

* Implemente um agente usando o algoritmo `MinMax` com poda alpha-beta, com limite de profundidade, capaz de jogar o jogo da velha.
* Você pode utilizar a mesma função de utilidade implementada anteriormente.
* Repita o processo de avaliação do agente, mas agora com a poda alpha-beta.
* Compare os resultados obtidos com a poda alpha-beta com os resultados obtidos sem a poda alpha-beta.
* Você deve encontrar uma forma gráfica para sumarizar os dados dos experimentos. 
* Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`.

## Entrega

* Para a implementação e entrega deste exercício nós vamos utilizar o Github Classroom. O link para para envio do projeto é este aqui [https://classroom.github.com/a/qTtNQURN](https://classroom.github.com/a/qTtNQURN). 

* A entrega é em equipes com até 4 integrantes e o  **prazo para a entrega** é 22/04/2024 (segunda-feira) até às 23:30 horas.