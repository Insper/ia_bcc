---
title: Inteligência Artificial e Robótica
subtitle: Design Review
author: Fabrício Barth 
institute: Insper
date: 01/2023
theme: insper
aspectratio: 169
...

## Objetivos

Ao final da disciplina o estudante será capaz de:

1. Descrever os conceitos, técnicas e métodos para o desenvolvimento de **Agentes Autônomos**.
2. Identificar **quais tipos de problemas podem ser resolvidos** através do uso de Agentes Autônomos. 
3. Criar soluções para alguns **problemas clássicos** desta área.
4. Especificar, desenvolver e testar projetos que façam uso de Agentes Autônomos para resolver **problemas complexos**.
5. Planejar e executar um trabalho em equipe, fornecendo e assimilando devolutivas.

# Como?

## Primeira semana

Através de uma dinâmica de grupo, envolvendo **exemplos e contra-exemplos de aplicações de IA**, os estudantes irão: 

1. Criar uma definição para *strong AI* (*general AI*).
2. Enumerar diferenças entre *strong AI* e *weak AI*.
3. Criar uma definição para **agente autônomo**.
4. Listar capacidades que um agente autônomo deve ter (ementa desta disciplina e de disciplinas futuras).
5. Listar característica de ambientes. 

## Output da primeira semana

:::::::::::::: {.columns}
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{img/agent_02.png}

:::
::: {.column width="50%"}

1. **Problem-solving**
2. Knowledge and reasoning
3. Learning
    1. Supervised Learning and Unsupervised Learning
    2. **Reinforcement Learning**
4. Communicating, perceiving, and acting
    1. Natural Language Processing
    2. Computer Vision
    3. **Robotics**

:::
::::::::::::::


## Output da primeira semana

:::::::::::::: {.columns}
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{img/agent_02.png}

:::
::: {.column width="50%"}

Ambientes:

1. *Single Agent*, determinístico, custo uniforme
2. *Single Agent*, determinístico, custo não uniforme
3. *Single Agent*, não-determinístico 
4. *Multi Agent* Competitivo, determinístico

Fora do escopo: *multi agent* colaborativo.

:::
::::::::::::::

## Ementa da disciplina

1. Definições de Agente Autônomo e resolução de problemas.
2. Estratégias de busca: algoritmos de busca cega e algoritmos informados. 
3. Heurísticas.
4. Implementação de agentes autônomos utilizando estratégias de busca.
5. Programação por restrições (CSP).
6. Ambientes competitivos e teoria de jogos. 
7. Algoritmo Min-Max e função de utilidade. 
8. Implementação de agentes autônomos para ambientes competitivos.
9. Aprendizagem por Reforço.
10. Implementação de agentes autônomos usando aprendizagem por reforço. 
11. Algoritmo Q-Learning. 
12. Implementações de agentes autônomos usando o projeto Gym.
13. Implementação de um agente robótico.

# Primeiro bloco: busca, busca informada e busca competitiva

## Questões e Exemplos de Problemas

:::::::::::::: {.columns}
::: {.column width="60%"}

* O que é relevante representar nos estados do mundo? Como os
    estados são estruturados (estrutura de dados) e qual o significado
    dela (dos campos)?
* Quais as operações sobre os estados?
* Qual a estimativa do tamanho do espaço de busca?
* Qual é a estimativa da árvore de busca?
* É necessário utilizar um algoritmo informado? Se sim, qual é a heurística? 
Existe heurística admissível? 

:::
::: {.column width="40%"}

* Aspirador de pó
* O homem, o lobo, o carneiro e o cesto de alface
* Banda U2 - problema de custo não uniforme
* Cavalo e tabuleiro de xadrez
* Problema das N rainhas

:::
::::::::::::::

## Implementação (1/2)

\includegraphics[width=1\textwidth]{img/agent_code.png}

## Implementação (2/2)

\includegraphics[width=0.7\textwidth]{img/agent_code_2.png}

## Conceitos explorados e a relação com outras disciplinas

* Algoritmos de Busca: Busca em Largura e Profundidade $\rightarrow$ **Técnicas de Programação**
* Recursão $\rightarrow$ **Técnicas de Programação**
* Busca em Profundidade Iterativa, Busca de Custo Uniforme, Busca Gananciosa, Busca A*
* Grafos e Árvores $\rightarrow$ **Algoritmos e Estrutura de Dados**
* Heurística
* Algoritmos de subida da montanha e outros relacionados com CSP
* Algoritmo Min-Max

# Segundo bloco: Aprendizagem por Reforço

## Aprendizagem por Reforço (RL)

* Para tratar problemas não determinísticos
* Heurística e Função de Utilidade que são aprendidas pelo próprio agente
* Agente Autônomo, Ambiente e **Reforço**
* Algoritmo *Q-Learning*
* Exemplo de programação dinâmica

## Implementação

````python
import gymnasium as gym
from QLearning import QLearning

env = gym.make("Taxi-v3", render_mode='ansi').env
env = gym.make('FrozenLake-v1', render_mode='ansi').env
env = gym.make("Blackjack-v1", render_mode='ansi')

qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
q_table = qlearn.train('data/q-table-taxi-driver.csv', 'results/actions_taxidriver')
````

````python
from kaggle_environments import make
env = make("tictactoe", debug=True)
````

# Terceiro bloco: Robótica

## Implementação de um agente robótico

\begin{center}
\includegraphics[width=1\textwidth]{img/labirinto.png}
\end{center}

## Avaliação

:::::::::::::: {.columns}
::: {.column width="50%"}

* Todos os projetos utilizam o Github Classroom.
* Alguns projetos fazem uso de testes automatizados.
* Alguns projetos são individuais, outros em grupo.

:::
::: {.column width="50%"}

\includegraphics[width=0.9\textwidth]{img/AI_projects_2022.png}

:::
::::::::::::::


