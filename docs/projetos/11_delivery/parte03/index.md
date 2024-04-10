# Interface gráfica do sistema de entrega de encomendas

Nesta parte do projeto você deverá implementar uma interface gráfica para o sistema de entrega de encomendas que você implementou nas entregas anteriores.

Quando terminado, o seu sistema deverá ser capaz de mostrar o mapa com as entregas que devem ser feitas e o entregador disponível. Também deverá mostrar a movimentação do entregador no mapa indo até a entrega, pegando a entrega e entregando a encomenda.

Esta interface gráfica deve permitir a adição de encomendas, clientes e a movimentação dos entregadores no mapa.

Uma vez editado o mapa, o sistema deve ser capaz de calcular a melhor rota para o entregador fazer as entregas. Não existe interação do usuário depois que o entregador começa a executar a sua lógica. 

A configuração do mapa não pode estar hard-coded no código. O mapa deve ser carregado de um arquivo de configuração ou definido via interface gráfica.

A sua entrega pode considerar um tamanho máximo de mapa de 30 por 30. 

A interface gráfica deve mostrar quem é o entregador, onde estão os bloqueios, onde está a encomenda, onde está o cliente da encomenda, a ação que o entregador está executando e o caminho que ele está seguindo. Também deve ficar claro na interface se o entregador está se movendo com a entrega ou não.

Quando você tiver isto pronto, por favor, chame o professor da disciplina para validar e fazer o:  

:new: check-point número 3.

## Itens do check-point 3

* Interface gráfica mostra onde entregador está
* Interface gráfica mostra que ação entregador está realizado
* Interface gráfica mostra onde estão os bloqueios
* Interface gráfica mostra onde está a encomenda e o cliente da encomenda
* Interface gráfica consegue mostrar mais que uma encomenda
* Interface gráfica mostra se entregador está com encomenda ou não
* Sistema permite a configuração do mapa: tamanho, obstáculos, onde o entregador está e onde as encomendas estão. Esta configuração não pode ser feita via código
* Sistema calcula a melhor rota para o entregador fazer as entregas e mostra o custo
* Depois que inicializado o processo de busca pela solução não será mais possível interagir com o sistema

[[Parte 1](../parte01/index.md)] [[Parte 2](../parte02/index.md)] [[Parte 4](../parte04/index.md)] [[Projeto](../index.md)]