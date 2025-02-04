# Implementando um Aspirador de Pó

## Configuração do ambiente

Para executar esta atividade você terá que criar um projeto e como dependência deste projeto instalar a biblioteca [AIGYM](https://pypi.org/project/aigyminsper/):

```bash
pip install aigyminsper
```

Esta biblioteca implementa diversos algoritmos de busca que serão utilizados ao longo da disciplina. Além disso, esta biblioteca permite o desenvolvimento de agentes inteligentes através de uma interface padrão.  

## Exercício: Aspirador de Pó

Para este exercício vamos utilizar o arquivo [AgentSpecification.py](./code/AgentSpecification.py).

* Faça uma cópia deste arquivo e chame ele de `AspiradorPo.py`, por exemplo.
* No método `__init__` defina a estrutura de dados que você especificou na aula passada. 
* No método `successors` codifique a execução das ações segundo o que você especificou na aula passada. **Dica**: cada novo estado é uma instância de um novo objeto da classe que é adicionado na lista retornada pelo método. 
* Codifique o comportamento do método `is_goal`. Ele deve retornar `True` quando encontrar um estado igual a meta. 
* O médoto `description()` retorna uma descrição do problema que está sendo resolvido. Por favor, altere o que está descrito no método. 
* Faça um retorno para o método `env()`. Peça para o professor explicar em sala de aula.
* Altere o método `main()` para que o mesmo chame a sua classe. 

??? warning "Conceitos que devem ser explorados neste exercício"

    Representação de um problema na forma de **estado**, **transição**, **grafo**

??? warning "Conceitos que devem ser explorados neste exercício"

    Algoritmos de Busca, começando com o algoritmo de busca em largura. 

??? hint "Importante!"

    Recomenda-se fortemente que todo estudante faça estas atividades em sua máquina. Os problemas podem ser discutidos em grupo, no entanto, cada aluno precisa ter a sua própria implementação.

## Exercício 2: Aspirador de Pó com 4 quartos.

Vamos implementar um aspirador de pó que atua em um ambiente com 4 quartos? Um quadrado $2 \times 2$? 

Mas, antes de implementar usando uma estrutura similar a descrita acima, responda as questões abaixo: 

* O que é relevante representar nos estados do mundo? Como os
    estados são estruturados (estrutura de dados) e qual o significado
    dela (dos campos)?
* Mostre como ficam representados os estados inicial e final
    segundo a representação adotada.
* Quais as operações sobre os estados?
    (detalhe como cada operação irá alterar os estados e quais as
    condições para cada operação ser executada)
* Qual a estimativa do tamanho do espaço de busca (número de
    estados possíveis)?

## Exercício 3: Aspirador de Pó com poltrona. 

Neste problema os quartos da casa podem possuir poltronas. Para limpar o quarto da casa que tem poltrona o agente deve antes de executar a ação limpar `virar` a poltrona. Claro que depois de limpar o agente deve também `desvirar` a poltrona para deixar o quarto em ordem. 

Para este problema considere um ambiente (casa) também com 4 quartos (um quadrado $2 \times 2$). 

Mas, antes de implementar usando uma estrutura similar a descrita acima, responda as questões abaixo: 

* O que é relevante representar nos estados do mundo? Como os
    estados são estruturados (estrutura de dados) e qual o significado
    dela (dos campos)?
* Mostre como ficam representados os estados inicial e final
    segundo a representação adotada.
* Quais as operações sobre os estados?
    (detalhe como cada operação irá alterar os estados e quais as
    condições para cada operação ser executada)
* Qual a estimativa do tamanho do espaço de busca (número de
    estados possíveis)?