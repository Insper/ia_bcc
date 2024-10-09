# Projeto intermediário 2024/2

## Descrição

O contexto e descricação do escopo deste projeto estão neste [arquivo](./Projeto_Intermediario_IA_2024_2.pdf). Por favor, leia com atenção o conteúdo deste arquivo antes de continuar. 

??? warning "Dúvidas? "
    Quais são as suas dúvidas sobre o escopo do projeto?

## Referências

Alguns links e arquivos que poderão ajudar na implementação do projeto: 

* [Link para a biblioteca DSSE](https://pfeinsper.github.io/drone-swarm-search/Documentation/docsCoverage.html#about).
* [Arquivo exemplo de como utilizar o ambiente de coverage](./src/coverage_example.py).
* [Arquivo exemplo de como simular o funcionamento de um agente considerando o ambiente pré-configurado 01](./src/execute_config_01.py).
* [Arquivo exemplo de como simular o funcionamento de um agente considerando o ambiente pré-configurado 02](./src/execute_config_02.py).

Arquivos que serão utilizados no projeto: 

* [Matriz de probabilidade para o ambiente 01 - considerando algum lugar próximo do Guarujá](./data/config_01.npy).
* [Matriz de probabilidade para o ambiente 02 - considerando algum lugar próximo de Florianópolis](./data/config_02.npy).


## Tarefas e Rubrica

Para a entrega deste projeto, cada equipe deverá realizar as tarefas que estão listadas na tabela abaixo. A tabela também indica a relação da atividade com a rubrica de avaliação.

| Tarefas | Rubrica |
|--------|---------|
|Entender o problema proposto e o ambiente de simulação, ou seja, a biblioteca [DSSE](https://pfeinsper.github.io/drone-swarm-search/Documentation/docsCoverage.html#about).| D|
|Fazer a configuração do repositório usando arquivo requirements.txt e um ambiente virtual. No arquivo requirements.txt deve conter todas as bibliotecas necessárias para a execução do projeto.|D|
|Implementar um agente que executa o *traditional maritime search pattern* em um ambiente com 1 agente.|D|
|Implementar um agente que executa o algoritmo *expanding square search* em um ambiente com 1 agente.|D|

Se o grupo realizar apenas um sub-conjunto das tarefas acima, o grupo receberá o conceito I.

| Tarefas | Rubrica |
|--------|---------|
|Implementar um agente que executa o algoritmo A* em um ambiente com 1 agente.|C|
|Executar os algoritmos acima considerando o ambiente pré-configurado 01 e o ambiente pré-configurado 02, e coletar os dados da execução.|C|
|O arquivo que executa as simulações deve receber três parâmetros: o ambiente, o algoritmo e a quantidade de agentes. A implementação deste script deve permitir que qualquer pessoa possa executar a qualquer momento qualquer combinação válida. Neste momento, a quantidade de agentes sempre será 1, mas para outras análise este valor poderá ser alterado.|C| 
|Os dados da execução devem ser salvos em um arquivo CSV. Um arquivo CSV para cada ambiente, cada algoritmo e quantidade de agentes. Os arquivos CSV precisam estar em uma pasta específica e devidamente identificados.|C|
|Para a criação dos gráficos deve-se utilizar um Jupyter Notebook. Este notebook deve ser salvo em uma pasta específica e devidamente identificado. Os gráficos gerados devem adotar o mesmo padrão dos gráficos apresentados no arquivo [Projeto_Intermediario_IA_2024_2.pdf](./Projeto_Intermediario_IA_2024_2.pdf).|C|

Para que um grupo obtenha determinado conceito, é necessário que todas as tarefas que compõem o conceito sejam realizadas, além das tarefas relacionadas aos conceitos anteriores.

| Tarefas | Rubrica |
|--------|---------|
|Implementar um agente que executa o *traditional maritime search pattern with 2 agents* em um ambiente com 2 agente.|B|
|Implementar um agente que executa o *traditional maritime search pattern with 4 agents* em um ambiente com 4 agente.|B|
|Executar os algoritmos *tradicional maritime search*, *expanding square search* e *A** considerando os ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes, e coletar os dados da execução.|B|
|Implementar um Jupyter Notebook que apresenta os gráficos para todos os cenários simulados. Os gráficos gerados devem adotar o mesmo padrão dos gráficos apresentados no arquivo [Projeto_Intermediario_IA_2024_2.pdf](./Projeto_Intermediario_IA_2024_2.pdf).|B|

| Tarefas | Rubrica |
|--------|---------|
| Criar um relatório que compara os algoritmos *tradicional maritime search*, *expanding square search* e *A** considerando os ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes. O relatório deve conter uma análise dos resultados obtidos. Para uma análise completa, este relatório precisa ter gráficos que comparam os algoritmos nos ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes. Ou seja, cada gráfico irá ter $n$ linhas onde $n$ é o número de algoritmos a serem comparados. |A|
| No relatório é necessário deixar claro qual foi a heurística utilizada no algoritmo *A** e qualquer outra informação relevante sobre os outros algoritmos. |A|

| Tarefas | Rubrica |
|--------|---------|
| Pesquisar por um algoritmo de busca específico para problemas de *Coverage Path Planning*, implementar este algoritmo e aplicar este algoritmo nos ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes. |A+|
| Criar um relatório que compara o algoritmo pesquisado com os algoritmos *tradicional maritime search*, *expanding square search* e *A** considerando os ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes. O relatório deve conter uma análise dos resultados obtidos. Para uma análise completa, este relatório precisa ter gráficos que comparam os algoritmos nos ambientes pré-configurado 01 e o ambiente pré-configurado 02, com 1, 2 e 4 agentes. Ou seja, cada gráfico irá ter $n$ linhas onde $n$ é o número de algoritmos a serem comparados. |A+|
| No relatório é necessário descrever o algoritmo pesquisado e informar as devidas referências. |A+|

## Regras para a entrega do projeto

* Para a implementação e entrega deste exercício nós vamos utilizar o Github Classroom. O link para para envio do projeto é: [https://classroom.github.com/a/xN_iRBUE](https://classroom.github.com/a/xN_iRBUE). 

* A entrega é em equipes com até 3 integrantes e o  **prazo para a entrega** é 13/10/2024 (domingo) até às 23:30 horas.