# Jogador de BlackJack

A biblioteca Gymnasium possui um ambiente que simula um jogo de [BlackJack (*Blackjack-v1*)](https://gymnasium.farama.org/environments/toy_text/blackjack/). A documentação deste ambiente está disponível neste link [https://gymnasium.farama.org/environments/toy_text/blackjack/](https://gymnasium.farama.org/environments/toy_text/blackjack/). 

## Atividades propostas: 

* Execute diversas vezes o arquivo [BlackJack_Manual.py](https://github.com/Insper/rl_code/blob/main/src/part_04/BlackJack_Manual.py) para entender como o ambiente funciona. Principalmente como a representação do espaço de estados funciona. 

* Implemente uma versão do algoritmo Q-Learning para o ambiente BlackJack. Importante perceber que o estado do BlackJack é representado por uma tupla de 3 elementos: (sua soma, carta do dealer, se você tem um Ás). De alguma forma você precisa transformar esta tupla em um número inteiro para poder usar como índice da q-table.

* Treine o seu agente usando o algoritmo Q-Learning e verifique o desempenho do mesmo.

* Implemente uma versão do algoritmo Sarsa para o ambiente BlackJack. Importante perceber que o estado do BlackJack é representado por uma tupla de 3 elementos: (sua soma, carta do dealer, se você tem um Ás). De alguma forma você precisa transformar esta tupla em um número inteiro para poder usar como índice da q-table.

* Treine o seu agente usando o algoritmo Sarsa e verifique o desempenho do mesmo.

## Perguntas 

* Como podemos obter um agente com o melhor desempenho possível? É possível criar um agente que ganha ou empata em no mínimo 85% dos jogos? Se sim, quais são os hiperparâmetros para este agente? Se não, qual é o melhor resultado encontrado? 

* É possível plotar a q-table? Este plot de q-table seria útil para um jogador de BlackJack real? Justifique a sua resposta. 

## Entrega 

* você deve criar um arquivo README.md informando os hiperparâmetros utilizados para o treinamento. Este arquivo README.md deve possuir um link para o plot da q-table.

* você deve entregar a sua implementação via Github Classroom no repositório: [https://classroom.github.com/a/ExQNdof6](https://classroom.github.com/a/ExQNdof6). Este respositório deve possuir o arquivo README.md, os arquivos python das implementações e a(s) q-table(s) gerada(s) pelo(s) algoritmo(s).


Exemplo de comparação entre algoritmos e hiperparâmetros utilizados no treinamento:

| Atributo / Algoritmo       |  Q-Learning     | Sarsa | 
|:----------------|:----------:|:----------:|
| alpha           |            |            |
| gamma           |            |            |
| epsilon         |            |            |
| epsilon_dec     |            |            |
| epsilon_min     |            |            |
| qtd_episodios   |            |            |


## Rubrica de avaliação

* Não terminou a implementação de nenhum dos algoritmos (Q-Learning ou Sarsa) e as suas respectivas avaliações $\rightarrow$ **Em Desenvolvimento (D)**.

* Implementou um dos algoritmos, treinou o agente para jogar BlackJack e avaliou o desempenho do agente executando diversas vezes o agente neste ambiente. Neste caso é necessário entregar a implementação, o arquivo README.md e a q-table treinada $\rightarrow$ **Básico (C)**

* Implementou e avaliou ambos os algoritmos, entregando a implementação, o arquivo README.md e as q-tables treinadas. Avaliou ambos os algoritmos, executando o jogo diversas vezes e medindo o desempenho dos agentes $\rightarrow$ **Esperado (B)**. 

* Implementou e avaliou ambos os algoritmos, entregando a implementação, o arquivo README.md e as q-tables treinadas. Além disso, entregou o gráfico que resume a q-table e explicou se é possível utilizar tal informação em uma situação real ou não $\rightarrow$ **Avançado (A)**.

## Deadline

O deadline para a entrega desta atividade é **23 de novembro de 2023 às 23:30 horas**. Este projeto é individual. 
