# Gabarito da prova final

## 1. Encontrando o menor caminho com algoritmos de busca (3 pontos)

Uma possível solução é apresentada no arquivo [my_agent.py](./src/my_agent.py).

A solução entregue deve passar por todos os testes descritos no arquivo de [testes](./src/test_my_agent_depois_entrega.py).

## 2. Encontrando o caminho com aprendizado por reforço (3 pontos)

1. Qual foi a política que o agente aprendeu a executar?

Dado o que é definido na função de reward, o agente aprende a não bater nas paredes e não sair do mapa. No entanto, como o primeiro exercício tem um objetivo fixo então o agente também consegue aprender a chegar no objetivo se os hiperparâmetros forem corretamente definidos. Mas não necessariamente pelo caminho mais curto. 

2. O que acontece se alterarmos os hiperparâmetros para $\alpha = 0.1, \gamma = 0.99, \epsilon = 0.8, \epsilon_{min} = 0.05, \epsilon_{dec} = 1, episodes = 1000$? Qual foi o comportamento do agente durante o treinamento? Depois de treinado o agente consegue alcançar o objetivo?

Como não existe decaimento do epsilon, pois $\epsilon_{dec}=1$, o agente durante o treinamento sempre vai escolher mais ações aleatórias do que ações baseadas na política aprendida. Isso faz com que o agente demore mais em cada episódio. Mas, dado a simplicidade do ambiente, o agente consegue aprender a não bater nas paredes e não sair do mapa. 

3. O que acontece se alterarmos os hiperparâmetros para $\alpha = 0, \gamma = 0.99, \epsilon = 0.8, \epsilon_{min} = 0.05, \epsilon_{dec} = 1, episodes = 1000$? Justifique a sua resposta. 

O agente não aprende em absoluto pois o valor de $\alpha$ é zero. Isso faz com que o agente não atualize os valores da tabela Q.

## 3. Problema de otimização (2 pontos)

Uma possível solução é apresentada no arquivo [Otimizacao.py](./src/Otimizacao.py).

## 4. Problema de tomada de decisão (1 ponto)

A decisão executada pelo agente será executar a ação **M**. 

## 5. Analisando ambientes (1 ponto)

### busca de menor caminho entre duas cidades 

single-agent, determinístico e A*

### um agente jogador de jogo da velha

multi-agent (competitivo), determinístico e minimax

### agente que é capaz de andar em um lago congelado

single-agent, estocástico e Q-learning ou Sarsa