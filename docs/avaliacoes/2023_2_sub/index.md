# Avaliação substitutiva 02/2023

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

Considere uma situação onde no ponto de origem temos 10 vigas de 50 metros, 20 vigas de 30 metros, 10 vigas de 10 metros e 5 vigas de 5 metros, qual é a sequência de viagens do ponto de origem ao ponto de destino que irá configurar o menor custo? E que custo é este?

Para esta questão você deverá: 

* especificar como os estados devem ser representados;
* especificar quais as operações que o seu agente sabe executar e qual o impacto delas no ambiente;
* especificar o que define o estado terminal;
* especificar o custo de cada ação;
* escolher um algoritmo que garanta soluções ótimas, e;
* implementar a solução usando a biblioteca **aigyminsper**.  

O programa implementado deverá receber os tipos e as quantidades de vigas no ponto de origem e retornar a sequência de ações. A sequência de ações deve informar de que ponto para qual ponto o caminhão está indo e quantas vigas ele está transportando em cada momento. No final deve ser informado o custo da solução em reais.  

### Web crawler (2 pontos)

O aplicativo `wget` é um web crawler disponível em sistemas operacionais do tipo *linux*. Com este aplicativo é possível informar uma `url` que será a base do *crawler*. A partir da `url` informada, o `wget` copia o conteúdo da página, identifica os links que estão nesta página, acessa o conteúdo destes links e copia o contéudo destas páginas de forma recursiva até encontrar um critério de parada. O critério de parada no caso do `wget` é a profundidade informada ao executar o comando.

Um código possível para o `wget` é apresentado abaixo: 

```python
def wget(url, profundidade):
    if profundidade > 0:
        armazena_conteudo(url)
        for nova_pagina in identifica_links(url):
            wget(nova_pagina, profundidade-1)
```

onde: 

* `armazena_conteudo(url)` é uma função que copia o contéudo da página para a máquina local, onde o `wget` está sendo executado. 
* `identifica_links(url)` é uma função que identifica todos os links na página - todas as tags `href`. 


Digamos que você precisa fazer o crawler de diversos conteúdos a partir de algumas páginas. Mas antes de fazer isto, você terá que fazer uma estimativa do tamanho de espaço necessário para armazenar todo o conteúdo. 

Os tópicos que você terá que armazenar são: 

* esportes: neste caso, você irá partir de uma única `url` e você sabe que todos os documentos que você irá baixar que estão relacionados com esta `url` tem **10 links** no seu conteúdo. Você também sabe que a profundidade configurada no `wget` para esportes será de **5**. E que cada documento documento tem o tamanho de 500 KBytes. Depois de executado o `wget` para esportes, quantos documentos (arquivos diferentes) serão armazenados no seu computador? Qual é o espaço que eles irão ocupar em MB? 

* cotidiano: neste caso, você irá partir de uma única `url` e você sabe que todos os documentos que você irá baixar que estão relacionados com esta `url` tem **3 links** no seu conteúdo. Você também sabe que a profundidade configurada no `wget` para o tema cotidiano será de **8**. E que cada documento documento tem o tamanho de 800 KBytes. Depois de executado o `wget` para cotidiano, quantos documentos (arquivos diferentes) serão armazenados no seu computador? Qual é o espaço que eles irão ocupar em MB? 

* Qual é a quantidade total de arquivos armazenados no seu computador? Qual é o espaço total que eles irão ocupar em MB? Justifique a sua resposta.

### Problema de otimização (3 pontos)

Considere um problema de otimização de uma função $f(x) = x^{2} + 8x$. Utilize um dos algoritmos de subida da montanha para encontrar o mínimo global desta função no intervalo $[-10,4]$. Você deve:

* utilizar uma das implementações existentes no pacote `aigyminsper.search.CSPAlgorithms`. 
* definir a forma para representação do estado.
* definir o método para geração dos sucessores.

Além da implementação, você deve informar qual é o valor de $x$ que minimiza a função $f(x) = x^{2} + 8x$.  


## Entrega dos itens da avaliação

Toda a prova deve ser submetida no Github Classroom através deste link: [https://classroom.github.com/a/0rG0rAYS](https://classroom.github.com/a/0rG0rAYS).

Os arquivos que precisam ser submetidos são: 

* `README.md`: onde você irá colocar as respostas para as questões que não envolvem implementação ou os complementos das demais questões. 
* `requirements.txt`: arquivo com todas as bibliotecas necessárias para as soluções que você irá entregar. 
* `Transporte.py`: arquivo com a solução para o problema da transportadora (questão 1).
* `Otimizacao.py`: arquivo com a solução para o problema de otimização. 

Não existe nenhum projeto de *template* e também não existem arquivos de testes. 

No caso das implementações, você deverá definir tudo: como os estados são representados, quais são os parâmetros do construtor da classe, quais são as ações e como elas afetam os estados, qual é o critério que retorna `true` para o método `is_goal()`, e assim em diante. 

O horário limite para entrega da prova é 11:50 do dia 13 de dezembro de 2023. Para fins de avaliação será considerado último `commit` no repositório. 


