# Sistema de entrega de encomendas que considera mais de uma entrega

Nesta versão deste projeto a equipe deverá considerar mais de um entrega no mapa. Um exemplo é apresentado na figura abaixo: 

<img src="img/mapa_01.png"> 

Neste caso, o cliente "vermelho" solicitou a comida "vermelha" e o cliente "verde" solicitou a comida "verde". Você deve considerar esta situação como sendo o mesmo instante de tempo, ou seja, o cliente "vermelho" e o cliente "verde" solicitaram a comida ao mesmo tempo. Para este caso, o seu sistema deve calcular o custo para atender a ambos os clientes e atender o cliente com menor custo primeiro. 

Para o mapa acima, a solução apresentada pelo seu módulo deve ser a seguinte:

```
Custo para atender o cliente vermelho: 14
Custo para atender o cliente verde: 24
O cliente vermelho será atendido.
```

A sua equipe deve criar vários cenários de testes para validar a implementação. Deve também considerar uma quantidade de entregas maior que 2. 

No caso acima, o entregador deve atender o cliente vermelho primeiro, pois o custo para atender o cliente vermelho é menor que o custo para atender o cliente verde. Depois de atender o cliente vermelho, o entregador deverá refazer o calculo do custo para atender os clientes existentes no mapa. Neste caso o sistema deverá imprimir: 

```
Custo para atender o cliente verde: 24
O cliente verde será atendido.
```

A forma de identificar o cliente não precisa ser por cores, pode ser por algum outro tipo de identificador alfanumérico.

Se o entregador tiver um número N de entregas para fazer então o procedimento apresentado acima deve ser repetido N vezes. 

Quando você tiver isto pronto, por favor, chame o professor da disciplina para validar e fazer o:  

:new: check-point número 2. 

## Itens do check-point 2

* Sistema calcula a melhor rota para o entregador fazer as entregas e mostra o custo
* Sistema consegue atender mais de um cliente em diferentes instantes de tempo
* A lógica de atendimento apresentada acima precisa estar correta

[[Parte 1](../parte01/index.md)] [[Parte 3](../parte03/index.md)] [[Parte 4](../parte04/index.md)] [[Projeto](../index.md)]


