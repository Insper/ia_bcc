# Avaliação substitutiva 01/2023

## Orientações gerais

* Quaisquer hipóteses relevantes devem ser **explicitamente formuladas**. Faz parte da avaliação a **correta interpretação** das questões. A **clareza** e a **objetividade** das respostas serão consideradas na avaliação. 

* Esta avaliação é **individual**. Em hipótese alguma você poderá fazer uso de material de colegas.

* Durante esta avaliação você poderá fazer uso do seu material e de material existente na internet. 

## Questões

Abaixo são apresentas as questões desta avaliação. Todas as questões envolvem implementação. No entanto, elas são independentes. Você poderá, por exemplo, implementar a segunda questão primeiro e depois fazer a primeira questão. 

### Transportando itens de um ponto ao outro (5 pontos)

Considere uma empresa de transportes que precisa transportar vigas de aço de um ponto de **origem** para um ponto de **destino**. No ponto de **origem** podem ter $N$ vigas de aço. Estas vigas de aço podem ser de 5 comprimentos diferentes: 50 metros, 30 metros, 10 metros, 5 metros e 1 metro. Cada caminhão responsável pelo transporte pode transportar até **3 vigas por viagem** e nunca pode estar vazio devido uma restrição técnica da carroceria do caminhão. Mesmo nas viagens de retorno, do destino para a origem, é necessário que o caminhão tenha pelo menos 1 viga na carroceria. 

O valor de cada viagem é calculado levando-se em consideração a maior viga transportada. Por exemplo, se o caminhão levar uma viga de 30 metros então o valor da viagem será de $30 \times 500$ reais, ou seja, 15.000,00 reais. Mas, se um caminhão levar 1 viga de 30 metros e outras duas vigas de 5 metros então o valor continua sendo de 15.000,00 reais porque o cálculo do custo da viagem só considera a viga de maior tamanho. Outro exemplo, ao transportar 1 viga de 50 metros, 1 viga de 10 metros e outra de 5 metros, o custo da viagem será de $50 \times 500$ igual a 25.000,00 reais. 

Considere uma situação onde no ponto de origem temos 2 vigas de 50 metros, 1 viga de 5 metros e 1 viga de 1 metro, qual é a sequência de viagens do ponto de origem ao ponto de destino que irá configurar o menor custo? E que custo é este?

Considere uma situação onde no ponto de origem temos 10 vigas de 50 metros, 20 vigas de 30 mestros, 10 vigas de 10 metros e 5 vigas de 5 metros, qual é a sequência de viagens do ponto de origem ao ponto de destino que irá configurar o menor custo? E que custo é este?

Para esta questão você deverá: 

* especificar como os estados devem ser representados;
* especificar quais as operações que o seu agente sabe executar e qual o impacto delas no ambiente;
* especificar o que define o estado terminal;
* especificar o custo de cada ação;
* escolher um algoritmo que garanta soluções ótimas, e;
* implementar a solução usando a biblioteca **aigyminsper**.  

O programa implementado deverá receber os tipos e as quantidades de vigas no ponto de origem e retornar a sequência de ações. A sequência de ações deve informar de que ponto para qual ponto o caminhão está indo e quantas vigas ele está transportando em cada momento. No final deve ser informado o custo da solução em reais.  

### Problema de caixeiro-viajante na forma de cavalo (5 pontos)

*Considerando um tabuleiro de xadrez (`8x8`) com um único cavalo, quais os movimentos que o cavalo deve fazer para percorrer todas as posições do tabuleiro uma única vez e retornar ao ponto de partida?* 

O problema descrito acima é um problema típico de caixeiro-viajante. É possível resolver este tipo de problema usando os algoritmos de busca vistos nesta disciplina. 

Mas, para resolver este tipo de problema usando algoritmos de busca você deve ser capaz de responder as seguintes questões: 

1. Como os estados do mundo devem ser representados? (0.5 pontos)
1. Considerando a representação adotada, qual é a quantidade de estados possíveis? (0.5 pontos)
1. Qual é o tamanho (profundidade) desta solução? Justifique a sua resposta. (0.5 pontos)
1. Qual é a ramificação do problema? Justifique a sua resposta. (0.5 pontos)
1. Qual é o tamanho da árvore? Justifique a sua resposta. (0.5 pontos)
1. É possível usar algoritmos de busca cega para este problema? Justifique a sua resposta. (0.5 pontos)

Implemente o problema do cavalo em um tabuleiro de xadrez usando a biblioteca **aigyminsper**. (2 pontos)

## Entrega dos itens da avaliação

Toda a prova deve ser submetida no Github Classroom através deste link: [https://classroom.github.com/a/9ZtxvcrG](https://classroom.github.com/a/9ZtxvcrG).

Os arquivos que precisam ser submetidos são: 

* `README.md`: onde você irá colocar as respostas para as questões que não envolvem implementação ou os complementos das demais questões. 
* `requirements.txt`: arquivo com todas as bibliotecas necessárias para as soluções que você irá entregar. 
* `Transporte.py`: arquivo que implementa a solução para o problema do transporte de vigas.  
* `Cavalo.py`: arquivo que implementa a solução para o problema do cavalo. 

Não existe nenhum projeto de *template* e também não existem arquivos de testes. 

No caso das implementações, você deverá definir tudo: como os estados são representados, quais são os parâmetros do construtor da classe, quais são as ações e como elas afetam os estados, qual é o critério que retorna `true` para o método `is_goal()`, e assim em diante. 

O horário limite para entrega da prova é 9:45 do dia 13 de junho de 2023. Para fins de avaliação será considerado último `commit` no repositório. 

