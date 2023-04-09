# Jogador de jogo da velha

## Pré-atividade

Responda as perguntas abaixo: 

1. O que é um ambiente competitivo de soma zero?
1. Qual o objetivo do algoritmo Min-Max? Em outras palavras, por que um agente autônomo que atua em um ambiente competitivo deve usar o algoritmo Min-Max?
1. O que é função de utilidade? Por que utilizar funções de utilidade? 
1. Qual é a relação da profundidade da árvore de busca do Min-Max com o desempenho final do agente? Existe correlação? Justifique a sua resposta.

## Objetivo da atividade

O objetivo desta atividade é implementar um jogador de jogo da velha. O ambiente que vamos utilizar para implementar este jogador é o `kaggle-environments`. 

## Tutorial sobre o kaggle-environments

Para instalar o pacote execute o comando:

```bash
pip install kaggle-environments
```

O código fonte deste pacote e alguma documentação está disponível [neste link](https://github.com/Kaggle/kaggle-environments). 

Além disso, [neste link](tictactoe.ipynb) tem um tutorial bem básico sobre o funcionamento deste ambiente. 

## Implementação 

1. Implemente um agente usando o algoritmo `MinMax com poda alpha-beta`, sem limite de profundidade, capaz de jogar o jogo da velha. 
1. Execute 200 jogos do seu jogador contra o jogador `random`, onde `100` jogos o seu jogador é o primeiro a jogar e `100` jogos onde o seu jogador é o segundo a jogar. 
1. Quantas partidas o seu jogador ganhou, empatou e perdeu? Espera-se que ele não tenha perdido nenhuma partida. 
1. Para cada jogada feita pelo seu jogador você deve medir quanto tempo ele gasta para tomar a decisão e calcular a média e o desvio padrão.

Toda a implementação e documentação sobre os resultados deve estar em um arquivo `ipynb`. Se a equipe entregar todos os itens listados acima então a nota será **B**. 

Para atingir a nota **A+** então a dupla terá que fazer todos os itens anteriores mais os itens listados abaixo: 

1. Implemente um agente usando o algoritmo `MinMax com poda alpha-beta`, **com** limite de profundidade, capaz de jogar o jogo da velha. Consequentemente, você terá que definir uma função de utilidade para o jogo da velha. 
1. Execute 200 jogos do seu jogador contra o jogador `random`, onde `100` jogos o seu jogador é o primeiro a jogar e `100` jogos onde o seu jogador é o segundo a jogar. 
1. Quantas partidas o seu jogador ganhou, empatou e perdeu? Espera-se que ele não tenha perdido nenhuma partida. 
1. Para cada jogada feita pelo seu jogador você deve medir quanto tempo ele gasta para tomar a decisão e calcular a média e o desvio padrão.

Perguntas que você precisa responder: 

1. Qual é o agente com melhor desempenho? `MinMax` sem limite de profundidade ou com limite de profundidade? Justifique a sua resposta. 
1. Qual é o agente mais rápido? É significantemente mais rápido? Justifique a sua resposta. 

Todo o código e respostas para as perguntas devem estas no mesmo arquivo `ipynb`. 

## Entrega

* Para a implementação e entrega deste exercício nós vamos utilizar o Github Classroom. O link para para envio do projeto é este aqui [https://classroom.github.com/a/v3HzDh0E](https://classroom.github.com/a/v3HzDh0E). 

* A entrega é em duplas e o  **prazo para a entrega** é 12/04/2023 (quarta-feira) até às 23:30 horas.