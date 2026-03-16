# Problema de empilhamento de blocos (*block world problem*)

Temos um conjunto de blocos identificados por letras (A, B, C, D, E, ...) que podem estar: 

* empilhados uns sobre os outros, ou
* sobre a mesa.

O objetivo é mover os blocos para alcançar uma configuração específica. Cada bloco pode ser movido para outra posição, mas apenas um bloco pode ser movido por vez. O custo para mover um bloco é 1.

## Exemplo de estado inicial e objetivo

Estado inicial: 

```
    A
    B       C
   ---     ---
   mesa    mesa
```

Queremos alcançar o seguinte estado objetivo:

```
    C
    B
    A
   ---
   mesa
```

## Regras clássicas

As regras clássicas são:

* Só é possível mover um bloco por vez.
* Um bloco só pode ser movido se não houver outro bloco sobre ele.
* Um bloco pode ser colocado:

    * na mesa
    * sobre outro bloco livre

Dado um estado qualquer, como este: 

```
    A
    B       C
   ---     ---
   mesa    mesa
```

As ações possíveis são:

* Mover o bloco A para a mesa
* Mover o bloco A para o topo da pilha onde está o bloco C
* Mover o bloco C para o topo da pilha onde está o bloco A

as ações **não** possíveis são:

* Mover o bloco B, pois o bloco A está sobre ele.
* Mover o bloco C para a mesa, pois ele já está sobre a mesa. Esta ação até poderia ser considerada possível, mas não faria sentido, pois o bloco C já está sobre a mesa.


## Entrega do exercício

Para a entrega deste exercício, considere cenários com até **5 blocos**.

* Defina como será a representação do estado, das ações e do custo.
* Explique a representação do estado escolhida e forneça um exemplo de estado inicial e estado objetivo.
* Defina duas heurísticas para o problema.
* Implemente o algoritmo A* para resolver o problema utilizando as heurísticas definidas.
* Teste o algoritmo A* com as heurísticas definidas em pelo menos 3 cenários diferentes, incluindo o cenário apresentado acima.
* Crie um script de teste para cada cenário, onde o script deve imprimir o caminho encontrado e o custo total do caminho.
* Compare os resultados obtidos com as heurísticas definidas e discuta qual delas é mais eficiente para resolver o problema. Se uma das heurísticas não for admissível, explique o motivo e discuta os resultados obtidos com ela.

Este trabalho deve ser entregue neste repositório [https://classroom.github.com/a/vwfirwdG](https://classroom.github.com/a/vwfirwdG) no Github Classroom até o dia **27/03/2026**, horas 23:30. Este trabalho pode ser realisado em equipes com até 3 pessoas. 

Todas as respostas para as perguntas acima devem ser fornecidas em um arquivo `README.md` e todo o código deve ser entregue também. Não esqueçam de incluir o nome dos integrantes da equipe no arquivo `README.md`.

De preferência, tentem usar a biblioteca `aigyminsper` para implementar esta atividade. 

## Informação adicional

Este problema poderia ser resolvido com programação declarativa (Prolog), usando uma representação como o exemplos abaixo:

```prolog
on(A,B)
on(B,table)
on(C,table)
clear(A)
clear(C)
```

Claro que faltam as regras para mover os blocos, mas isto não é escopo desta disciplina. 
