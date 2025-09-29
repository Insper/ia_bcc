# Projeto Intermediário - 2025/02

Na [avaliação intermediária](prova.pdf) vocês tiveram que responder diversas questões sobre como desenvolver um VANT (Veículo Aéreo Não Tripulado) autônomo usando os conceitos vistos nesta disciplina.

Neste projeto, vocês deverão implementar este VANT autônomo em um simulador 3D. 

OS marcos deste projeto são: 

* Implementar o VANT da forma como foi descrito na avaliação intermediária.
* Implementar o VANT da forma como foi descrito na avaliação intermediária, mas agora com a capacidade de evitar obstáculos.
* Implementar uma forma gráfica para visualizar o ambiente 3D, o VANT e sua trajetória e os obstáculos.
* Implementar um agente que ao invés de ter acesso a todas as informações do ambiente, ele só tem acesso a informações parciais - algo que é muito mais próximo da realidade.

Cada marco deve ser implementado de forma incremental, ou seja, vocês devem começar implementando o primeiro marco e só depois passar para o próximo. A validação de cada marco deverá ser feita com o professor em sala de aula ou em horário de atendimento.

A seguir cada marco é descrito com mais detalhes.

## Primeiro marco: VANT autônomo

O VANT deve ser capaz de sair de um ponto inicial qualquer e chegar em um ponto final qualquer, ambos definidos no início da simulação. Lembre-se que o VANT sabe executar seis ações: mover para frente, mover para trás, ir para esquerda, ir para direita, subir e descer. O VANT também sabe a sua posição atual e a posição do ponto final.

Ao realizar esta tarefa, a equipe tem **conceito D**. Não é necessário implementar nenhuma visualização gráfica, basta um log com impressões no terminal mostrando a posição do VANT a cada passo e quando ele chegar no ponto final.

## Segundo marco: evitar obstáculos colocados no espaço de forma aleatória

Neste marco, o VANT deve ser capaz de evitar obstáculos que são colocados no espaço de forma aleatória. O VANT continua sabendo a sua posição atual e a posição do ponto final, mas agora ele também sabe a posição dos obstáculos. O VANT deve ser capaz de planejar uma rota que evite os obstáculos e chegue no ponto final.

Ao realizar esta tarefa, a equipe tem **conceito C**. Não é necessário implementar nenhuma visualização gráfica, basta um log com impressões no terminal mostrando a posição do VANT a cada passo e quando ele chegar no ponto final.

## Terceiro marco: visualização gráfica

Neste marco, o VANT deve ser capaz de evitar obstáculos que são colocados no espaço de forma aleatória. O VANT continua sabendo a sua posição atual e a posição do ponto final, mas agora ele também sabe a posição dos obstáculos. O VANT deve ser capaz de planejar uma rota que evite os obstáculos e chegue no ponto final.

Ao realizar esta tarefa, a equipe tem **conceito B**. É necessário **implementar uma visualização gráfica que mostre o ambiente 3D, o VANT, sua trajetória e os obstáculos**.

## Quarto marco: agente com percepção parcial

Neste marco, o VANT deve ser capaz de evitar obstáculos que são colocados no espaço de forma aleatória. O VANT ainda sabe a sua posição atual e a posição do ponto final, mas agora ele não consegue mais enxergar todo o mapa. O VANT só consegue enxergar o mapa que está em um raio de 5 unidades de distância a partir da sua posição atual. O VANT deve ser capaz de planejar uma rota que evite os obstáculos e chegue no ponto final. Para isso, você deve implementar alguma estratégia de busca online. 

O conceito de busca online será explicado em sala de aula.

Ao entregar esta tarefa, a equipe tem **conceito A**. É necessário **implementar uma visualização gráfica que mostre o ambiente 3D, o VANT, sua trajetória e os obstáculos**.

## Conceito "*plus*" (+)

Para ter um conceito "*plus*" (+), a solução não pode ter mais obstáculos aleatórios no espaço. Os obstáculos devem representar o relevo de uma determinada região, com montanhas, vales, etc. 

## Entrega  

A entrega do código deve ser feita no [Github Classroom](https://classroom.github.com/a/4h_amUTp) até o dia **08/10/2025**. As validações precisam ser feitas com o professor em sala de aula ou em horário de atendimento. O projeto deve ser implementado em [duplas já definidas](lista_duplas.md). 


