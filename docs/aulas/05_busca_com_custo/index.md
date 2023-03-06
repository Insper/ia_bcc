# Revisão do exercício anterior e novo exercício

Considerando [este exercício](../04_x_buscas/index.md#atividade-de-laboratório), quais são as respostas certas para as perguntas abaixo: 

* Segundo o que discutimos em sala de aula, quais destes algoritmos são ótimos? Os resultado encontrados neste exercício são coerentes com está informação? Justifique a sua resposta.

* Segundo o que discutimos em sala de aula, quais destes algoritmos são completos? Os resultado encontrados neste exercício são coerentes com está informação? Justifique a sua resposta.

* Teve algum algoritmo que travou por falta de memória no seu computador? Se sim, qual é a explicação?

* Qual é o algoritmo que tem um tempo de processamento menor? Justifique a sua resposta.

# Banda U2

Considere o seguinte problema: 

A banda U2 tem um concerto que começa daqui a 17 minutos e
  todos precisam cruzar uma ponte par chegar lá. Todos os 4
  participantes estão do mesmo lado da ponte. É noite. Só
  há uma lanterna. A ponte suporta, no máximo, duas
  pessoas. Qualquer pessoa que passe, uma ou duas, deve passar com a
  lanterna na mão. A lanterna deve ser levada de um lado para outro
  e não ser jogada. Cada membro da banda tem um tempo diferente
  para passar de um lado para o outro. O par deve andar no tempo do
  menos veloz: Bono: 1 minuto para passar; Edge: 2 minutos para
  passar; Adam: 5 minutos para passar; e Larry: 10 minutos para
  passar.

O problema consiste em ter os quatro elementos da banda do outro lado
da ponte no menor tempo possível.

Implemente um agente autônomo que consegue resolver este problema. Antes de iniciar a implementação, pense na resposta para as seguintes perguntas: 

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
* Que algoritmo de busca pode ser utilizado para resolver este problema considerando que
a solução apresentada precisa ser ótima? 

Implemente uma classe chamada `Solver` que resolve este problema. Esta classe precisa ter um método `main` com a seguinte assinatura: 

```python
def main(bono, edge, adam, larry, lanterna)
```

As variáveis bono, edge, adam, larry e lanterna são variáveis booleanas. Quando os valores são `False` significa que os mesmos estão do lado esquerdo do rio. Se os valores forem `True` significa que as pessoas ou a lanterna estão do lado direito do rio. 

## Formato de entrega

* Para a implementação e entrega deste exercício nós vamos utilizar o [Github Classroom](https://classroom.github.com/a/1b1ermRX). 

* O link para o enunciado é este aqui [https://classroom.github.com/a/1b1ermRX](https://classroom.github.com/a/1b1ermRX). Através deste link você consegue baixar o repositório e começar a sua codificação. 

* **Prazo para a entrega**: 08/03/2023 (quarta-feira) até às 23:00 horas. 

## Cuidados! 

* Execute os testes na sua máquina local antes de fazer o `push` para o Github Classroom.

* Ao fazer o `push` da sua solução, certifique-se que a solução passou por todos os testes. Você consegue ver isto na aba `actions` do seu repositório.  

## Rubrica de avaliação

| Conceito | Descrição |
|:--------:|:----------|
| A+       | Preencheu os requisitos para A e apresentou uma solução bem projetada e um código bem escrito |
| A        | Submeteu uma solução que consegue encontrar uma solução para o problema | 
| D        | Submeteu uma solução, mas a mesma não consegue encontrar uma solução para o problema |   

## Referências

O material utilizado para esta aula está nos slides 29 até 31 do conjunto de slides abaixo: 

<embed src="../../referencias/03_algoritmos_busca/busca_versaoFabricio.pdf" type="application/pdf" width="600" height="300">
