# Ambientes não-determinísticos
    
O ambiente [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a tarefa e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a tarefa com 0 pontos de reward. Cada ação que não leva para um estado terminal tem reward igual a 0.  

Neste ambiente o agente consegue executar 4 ações: ir para cima, ir para baixo, ir para esquerda e ir para direita. **Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo**, por exemplo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico.

O ambiente Frozen Lake está disponível no pacote `gymnasium` com duas configurações: 4x4 e 8x8. 

```python
import gymnasium as gym
env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=True).env
env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
```

A função de recompensa é dada por: 

\begin{equation}
R(s_{i}, A) = \begin{cases}
    1, & \text{se } s_{i} = \text{objetivo} \\
    0, & \text{se } s_{i} = \text{buraco} \\
    0, & \text{caso contrário}
    \end{cases}
\end{equation}

Os estados terminais são o objetivo e os buracos. Mas se o agente fizer mais de 100 movimentos no ambiente $4 \times 4$ ou mais de 200 movimentos no ambiente $8 \times 8$ então o episódio termina com `truncated` igual a `True` sem `reward` positivo ou negativo.

## Perguntas

* É possível treinar um agente capaz de atuar no ambiente do Frozen Lake? Ou seja, é possível treinar um agente capaz de atuar em um mundo **não-determinístico**?

* Qual é o melhor algoritmo e os melhores hiperparâmetros para treinar um agente capaz de atuar no ambiente do Frozen Lake? Considerando ambas as configurações: $4 \times 4$ e $8 \times 8$.

## Método

Para responder as perguntas acima você deve treinar um agente capaz de atuar no ambiente do Frozen Lake e comparar a curva de aprendizado do agente treinado com a curva de aprendizado de outros agentes treinados com diferentes algoritmos e hiperparâmetros. 

Você deve treinar o agente com os algoritmos Q-Learning e SARSA escolhendo duas configurações de hiperparâmetros para cada algoritmo. Ou seja, você irá comparar a curva de aprendizagem de 4 agentes diferentes para o ambiente $4 \times 4$ e 4 agentes diferentes para o ambiente $8 \times 8$.

**Detalhe importante**: neste ambiente o reward é apenas 0 ou 1. Nesta caso, a melhor abordagem é comparar a curva de aprendizagem dos agentes treinados usando uma média móvel dos rewards obtidos ao longo do treinamento.

Após treinar os agentes você deve utilizar o agente com melhor desempenho para o ambiente $4 \times 4$ e para o ambiente $8 \times 8$ e executar 100 vezes em ambos os ambientes e calcular a quantidade de vezes que o agente chegou até o destino final sem cair no buraco.

## Artefatos que devem ser entregues

Cada equipe deve entregar os seguintes artefatos: 

* Relatório com os gráficos das curvas de aprendizado dos agentes treinados e dados sobre o desempenho do melhor agente no ambiente (quantidade de vezes que o agente chegou até o destino final sem cair no buraco).

* Todos os códigos utilizados para executar os experimentos.

* Arquivo README.md descrevendo como executar o experimento. 

A entrega deve ser feita através do [Github Classroom](https://classroom.github.com/a/4J2eATAH). O trabalho é em equipe com até 4 pessoas.

### Rubrica de avaliação

Os itens para a avaliação são apresentados abaixo:

| Número | Descrição |
|:-------|:----------|
| 1 | implementou o algoritmo Sarsa|
| 2 | implementou o algoritmo Q-Learning|
|3 | realizou experimentos com no mínimo 2 configurações de hiperparâmetros para o ambiente $4 \times 4$ usando o algoritmo Sarsa|
|4 | realizou experimentos com no mínimo 2 configurações de hiperparâmetros para o ambiente $4 \times 4$ usando o algoritmo Q-Learning|
|5 | realizou experimentos com no mínimo 2 configurações de hiperparâmetros para o ambiente $8 \times 8$ usando o algoritmo Sarsa|
|6 | realizou experimentos com no mínimo 2 configurações de hiperparâmetros para o ambiente $8 \times 8$ usando o algoritmo Q-Learning|
|7 | entregou código bem organizado e um arquivo README.md com instruções claras sobre como executar os experimentos| 
|8 | apresentou os resultados dos experimentos com o ambiente $4 \times 4$ de forma clara e objetiva, incluindo o uso de gráfico|
|9 | apresentou os resultados dos experimentos com o ambiente $8 \times 8$ de forma clara e objetiva, incluindo o uso de gráfico|
|10 | apresentou um texto breve descrevendo os experimentos realizados e os resultados alcançados|
|11 | treinou um agente capaz de encontrar o caminho em no mínimo 70% das vezes em apenas uma dimensão do ambiente| 
|12 | treinou um agente capaz de encontrar o caminho em no mínimo 70% das vezes para ambas as dimensões de ambientes|

Segue lista de itens que devem ser entregues para alcançar cada conceito: 

| Conceito | Descrição |
|:--------:|:----------|
| I | Só entregou 1 e 2, sem conectar com os ambientes |
| D | Entregou um dos itens: 3, 4, 5 ou 6 |
| C | Entregou todos os itens de 1 até 6 |
| C+ | Entregou todos os itens de 1 até 7 | 
| B | Entregou todos os itens de 1 até 9 |
| B+ | Entregou todos os itens de 1 até 10 | 
| A | Entregou todos os itens de 1 até 10 e conseguiu ou o item 11 ou o item 12|
| A+ | Conseguiu entregar todos os itens | 


### Prazo de entrega

O prazo para a entrega desta atividade é **9 de maio de 2024 (quinta-feira) até às 11:30 horas da manhã**. 