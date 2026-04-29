# Aprendizagem por Reforço

Esta APS tem como objetivo exercitar os conceitos de Aprendizagem por Reforço utilizando dois ambientes da biblioteca Gymnasium: `CliffWalking` e `FrozenLake`. O ambiente `CliffWalking` já foi discutido em sala de aula.

O ambiente `FrozenLake` é um ambiente de grade onde o agente deve aprender a navegar de um ponto de partida até um objetivo, evitando buracos. O agente pode se mover para cima, baixo, esquerda ou direita, e recebe recompensas por alcançar o objetivo ou penalidades por cair em buracos. Este ambiente é muito parecido com todos os ambientes já vistos neste curso, exceto por um fato: ele é **não determinístico**. Isso significa que, ao escolher uma ação, o agente pode não se mover na direção desejada. Por exemplo, se o agente escolher mover-se para a direita, ele pode acabar se movendo para baixo ou para cima com uma certa probabilidade. Essa característica torna o ambiente mais desafiador e realista, exigindo que o agente aprenda a lidar com a incerteza.

Nesta APS, você irá utilizar o algoritmo Q-Learning e o algoritmo SARSA para treinar agentes nesses ambientes. O objetivo é comparar o comportamento dos agentes treinados com esses dois algoritmos e analisar as diferenças em suas políticas de ação.

## Ambiente CliffWalking

Para este ambiente você deve treinar um agente utilizando o algoritmo Q-Learning e um agente utilizando o algoritmo SARSA. Ambos os agentes depois de treinados não podem cair no penhasco, ou seja, não podem receber a recompensa de -100. Para isso, você deve ajustar os hiperparâmetros dos algoritmos para garantir que os agentes aprendam a chegar no destino sem cair no penhasco. Como teste, você deve executar cada agente por 100 episódios e plotar o gráfico de recompensa acumulada ao longo dos episódios para ambos os agentes. Em nenhum episódio os agentes devem receber a recompensa de -100.

Outra análise que você deve fazer é comparar as políticas de ação dos agentes treinados. Para isso, você deve criar um gif animado que mostre o comportamento dos agentes treinados no ambiente. O gif deve mostrar o agente se movendo pelo ambiente e tomando decisões com base em sua política de ação. Você deve comparar os gifs dos agentes treinados com Q-Learning e SARSA para analisar as diferenças em suas políticas de ação.

Você deve responder as seguintes perguntas: 

* Qual algoritmo, Q-Learning ou SARSA, apresentou um comportamento mais seguro em relação ao penhasco? Justifique sua resposta com base nos resultados obtidos.
* Se houver diferenças significativas entre as políticas de ação dos agentes treinados com Q-Learning e SARSA, explique por que elas podem ter ocorrido.

## Ambiente FrozenLake

Para este ambiente, você deve treinar um agente utilizando o algoritmo Q-Learning e um agente utilizando o algoritmo SARSA. O objetivo é comparar o comportamento dos agentes treinados com esses dois algoritmos e analisar as diferenças em suas políticas de ação. Para isso, você deve ajustar os hiperparâmetros dos algoritmos para garantir que os agentes aprendam a chegar no destino sem cair nos buracos. Como teste, você deve executar cada agente por 100 episódios 100 vezes e contar o número de vezes que cada agente alcança o objetivo. Desta forma, você terá para cada agente 100 valores de sucesso (alcançar o objetivo). Você deve calcular a média e o desvio padrão dos valores de sucesso para ambos os agentes. 

Outra análise que você deve fazer é comparar as políticas de ação dos agentes treinados. Para isso, você deve analisar a q-table gerada por cada agente e identificar as ações preferidas em cada estado. Você deve comparar as q-tables dos agentes treinados com Q-Learning e SARSA para analisar as diferenças em suas políticas de ação.

Você deve responder as seguintes perguntas:

* Qual algoritmo, Q-Learning ou SARSA, treinou o melhor agente para o ambiente FrozenLake? Justifique sua resposta com base nos resultados obtidos.
* Se houver diferenças significativas entre as políticas de ação dos agentes treinados com Q-Learning e SARSA, explique por que elas podem ter ocorrido. Considere a natureza não determinística do ambiente FrozenLake em sua resposta.
* Explique a política de ação preferida por cada agente em um estado específico do ambiente FrozenLake. Justifique por que cada agente pode ter desenvolvido essa política com base no algoritmo utilizado e na natureza do ambiente.

## Entrega

A entrega deve ser feita via Github Classroom, neste repositório [https://classroom.github.com/a/9qG0O12R](https://classroom.github.com/a/9qG0O12R). O repositório deve conter um arquivo `README.md` com as respostas para as perguntas propostas e gifs gerados. Além disso, o repositório deve conter todos os códigos utilizados para treinar e avaliar os agentes dentro de um único diretório chamado `src`. Os gifs gerados ou imagens devem ser salvos dentro de um diretório chamado `img`. O código deve ser bem documentado e organizado para facilitar a compreensão. Certifique-se de incluir instruções claras sobre como executar o código e reproduzir os resultados obtidos no arquivo README.md.

## Regras e prazo para entrega

* A entrega deve ser feita até o dia **30 de abril de 2026 às 23:45**. AS entregas feitas após esse prazo não serão aceitas, a menos que haja uma justificativa válida e prévia aprovada pelo professor.
* Este projeto pode ser feito em duplas ou individualmente. O arquivo README.md deve conter o nome dos integrantes da dupla, caso seja o caso. Ou o nome do aluno, caso seja individual.

## Referências

* Aulas sobre Aprendizagem por Reforço ministradas durante o curso.
* Documentação do Gymnasium: https://gymnasium.farama.org/