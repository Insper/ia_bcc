# Projeto 2: Conceitos básicos sobre reinforcement learning e ambientes não determinísticos

Considere o ambiente Taxi-v4 do Gymnasium, onde um táxi deve pegar e deixar passageiros em locais específicos de uma grade. Treine um agente utilizando Q-learning para aprender a política ótima de navegação no ambiente. Utilize valores de hiperparâmetros que possibilitem o aprendizado rápido e eficiente do agente.

1) Execute cinco vezes o treinamento do agente utilizando Q-learning e registre o reward acumulado obtido em cada episódio em cada execução. Ao final crie um plot que apresenta a curva de aprendizado do agente ao longo dos episódios. Neste plot você deve deixar claro qual é a meta de reward acumulado que o agente deve alcançar.

2) Após o treinamento, utilize a q-table aprendida para executar o agente no ambiente. Registre o número de timesteps necessários para que o agente complete a tarefa em cada execução. Execute 100 vezes e calcule a média e o desvio padrão dos timesteps necessários.

Depois de feito as atividades 1 e 2, treine um segundo agente com o algoritmo Sarsa e repita as mesmas análises: registre o reward acumulado durante o treinamento e o número de timesteps necessários para completar a tarefa no ambiente. Compare os resultados obtidos com os do agente treinado com Q-learning. Para comparar os agentes, considere tanto a eficiência no aprendizado quanto o desempenho final no ambiente. Utilize os mesmos valores de hiperparâmetros utilizados no treinamento do agente com Q-learning.

3) Discuta as diferenças observadas entre os agentes treinados com Q-learning e Sarsa, considerando tanto a eficiência no aprendizado quanto o desempenho final no ambiente. Faça uso de um único gráfico para comparar as curvas de aprendizado dos dois agentes.

## Ambiente não determinístico

No ambiente Taxi-v4, as ações do agente podem não ter efeito determinístico, ou seja, a execução de uma ação pode não levar sempre ao mesmo resultado. Isso introduz incerteza no aprendizado do agente, tornando o problema mais desafiador e exigindo que o agente aprenda uma política robusta que maximize o reward esperado mesmo diante da aleatoriedade do ambiente.

Ao usar o parâmetro `is_rainy=True` no ambiente Taxi-v4 torna o ambiente não determinístico: 

```python
env = gym.make("Taxi-v4", is_rainy=True, render_mode="human", rainy_probability=0.6).env
```

Será que a q-table aprendida em um ambiente determinístico ainda será eficaz em um ambiente não determinístico? Experimente executar o agente utilizando a q-table aprendida no ambiente com `is_rainy=True, rainy_probability=0.6` e observe o desempenho. Discuta os resultados obtidos e como a aleatoriedade do ambiente afeta a política aprendida pelo agente.

4) Utilize a q-table aprendida para executar o agente no ambiente não determinístico. Registre o número de timesteps necessários para que o agente complete a tarefa em cada execução. Execute 100 vezes e calcule a média e o desvio padrão dos timesteps necessários. Teve diferença no desempenho em relação ao ambiente determinístico? Discuta os resultados obtidos.

5) Sabendo que o ambiente do Táxi pode ser não determinístico quando `is_rainy=True, rainy_probability=0.6`, treine os agentes utilizando Q-learning e Sarsa nesse ambiente e compare o desempenho obtido com o desempenho no ambiente determinístico. Teve diferença? Discuta os resultados obtidos.

## Entrega

A entrega do projeto deve incluir:

- Código utilizado para treinar os agentes com Q-learning e Sarsa, tanto no ambiente determinístico quanto no não determinístico.
- Um relatório em jupyter notebook apresentando: 
  - Gráficos que apresentem as curvas de aprendizado dos agentes.
  - Tabelas ou resumos com os resultados obtidos, incluindo o número de timesteps médios necessários para completar a tarefa e desvios padrão.
  - Discussão sobre as diferenças observadas entre os agentes treinados com Q-learning e Sarsa, considerando eficiência no aprendizado e desempenho final.
  - Discussão sobre o impacto do não determinismo no desempenho dos agentes e na política aprendida.
  - Conclusões gerais sobre o comportamento dos agentes nos diferentes ambientes.

Todos estes itens devem estar em um único repositório no GitHub. As equipes deverão entregar o link para o repositório via blackboard até o dia 04/11/2026 às 23 horas. Cada equipe deve ser formada com no máximo 4 integrantes. 