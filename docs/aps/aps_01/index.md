# Problema dos cadeados

![Cadeado com 4 números](img/cadeado_4digitos.svg){ .lock-inline }

O objetivo deste problema é encontrar a combinação correta para abrir um cadeado, onde a combinação é composta por dois números. A cada passo, é possível incrementar um dos números em 1. O desafio é encontrar a combinação correta em um número mínimo de passos.

Os estados são representados por um vetor de dois números, e as ações possíveis são incrementar o primeiro número ou o segundo número. O estado inicial é (0, 0) e o estado objetivo é a combinação correta do cadeado.

Considerando que os números possíveis para cada posição do cadeado são de 0 a 9, o espaço de busca é finito, mas pode ser grande dependendo da combinação correta. O problema pode ser resolvido utilizando algoritmos de busca em Largura, Profundidade, Profundidade Iterativa, entre outros. A escolha do algoritmo de busca pode influenciar o desempenho da solução, especialmente em termos de tempo e memória.

Considerando que os números possíveis para cada posição do cadeado são de 0 a 9, qual é a profundidade máxima da árvore de busca para este problema? Qual é a ramificação do problema? 

<div class="lock-clear"></div>

## Atividade de implementação

Usando a biblioteca `aigyminsper`, implemente a classe `Cadeado2` que representa o estado do problema dos cadeados. A classe deve herdar de `State` e implementar os métodos necessários para definir os sucessores, verificar se o estado é o objetivo, fornecer uma descrição do problema e calcular o custo das ações.

Como os estados são representador por um vetor, é importante que no método `successors` sejam criados novos objetos `Cadeado2` para cada ação possível, garantindo que o estado atual não seja modificado. Além disso, é necessário fazer uma cópia do vetor de números antes de modificá-lo para criar os sucessores, por exemplo: 

```python
import copy

temp = copy.deepcopy(self.numeros)
temp[0] += 1 # Incrementa o primeiro número
# e entao usa ele para criar o sucessor
```

Depois de implementada a classe `Cadeado2`, utilize um algoritmo de busca, como a busca em largura, para encontrar a combinação correta do cadeado a partir do estado inicial (0, 0) até o estado objetivo (1, 3). Imprima o caminho encontrado e o custo total da solução.

Por exemplo, para este código: 

```python
def main():
    inicio = [0,0]
    fim = [1,3]
    print(f"Início: {inicio}, Fim: {fim}")
    state = Cadeado2('', [0, 0], [1, 3])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print('Nao achou solucao')
```

A saída deve ser: 

```
Início: [0, 0], Fim: [1, 3]
Achou!
 ; [+1,_] ; [_,+1] ; [_,+1] ; [_,+1]
Custo: 4
```

Faça vários testes para garantir que a implementação está correta. Por exemplo, usando algoritmos diferentes: 

```python
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, m=10)
```

E parâmetros que permitem visualizações diferentes do processamento: 

```python
    result = algorithm.search(state, show_process=True)
``` 

## Medindo tempo e memória de execução

Utilize a biblioteca `time` para medir o tempo de execução do algoritmo de busca. Para medir o uso de memória, você pode usar a biblioteca `memory_profiler`. Certifique-se de instalar a biblioteca `memory_profiler` usando pip:

```
pip install memory_profiler
```
Em seguida, você pode usar o decorador `@profile` para medir o uso de memória da função que executa a busca. Por exemplo:

```python
from memory_profiler import profile

@profile(precision=4)
def main():
    inicio = [0,0]
    fim = [1,3]
    print(f"Início: {inicio}, Fim: {fim}")
    state = Cadeado2('', [0, 0], [1, 3])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print('Nao achou solucao')
```

O formato de saída do `memory_profiler` mostrará o uso de memória linha por linha, permitindo que você identifique quais partes do código estão consumindo mais memória, por exemplo: 

```python
42     77.1 MiB      0.0 MiB           1       print(f"Início: {inicio}, Fim: {fim}")
    43     77.1 MiB      0.0 MiB           1       state = Cadeado2('', inicio, fim)
    44     77.1 MiB      0.0 MiB           1       algorithm = BuscaLargura()
    45     81.3 MiB      4.3 MiB           1       result = algorithm.search(state)
    46     81.3 MiB      0.0 MiB           1       if result != None:
    47     81.3 MiB      0.0 MiB           1           print('Achou!')
    48     81.3 MiB      0.0 MiB           1           print(result.show_path())
    49     81.3 MiB      0.0 MiB           1           print(f"Custo: {result.g}")
```

Como podemos ver, para este exemplo, a linha que executa a busca (`result = algorithm.search(state)`) é a que mais consome memória, o que é esperado, pois é onde ocorre a expansão dos nós e o armazenamento dos estados visitados. O uso de memória pode variar dependendo do algoritmo de busca utilizado e da profundidade da solução encontrada.

Para medir o tempo de execução, você pode usar a função `time()` do módulo `time` para registrar o tempo antes e depois da execução do algoritmo de busca. Por exemplo:

```python
import time
from memory_profiler import profile

@profile(precision=4)
def main():
    inicio = [0,0]
    fim = [1,3]
    print(f"Início: {inicio}, Fim: {fim}")
    state = Cadeado2('', inicio, fim)       
    algorithm = BuscaLargura()
    start_time = time.time()  # Início da medição de tempo
    result = algorithm.search(state)
    end_time = time.time()  # Fim da medição de tempo
    execution_time = end_time - start_time  # Cálculo do tempo de execução
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(f"Custo: {result.g}")
    else:
        print('Nao achou solucao')
    print(f"Tempo de execução: {execution_time:.4f} segundos")
```

## Medindo o tempo e memória de execução para diferentes profundidades

Teste a implementação do problema dos cadeados para diferentes combinações de fim, variando a profundidade da solução. Meça o tempo e a memória de execução para cada caso e analise como esses recursos são afetados pela profundidade da solução encontrada. Considere os algoritmos de busca em largura, profundidade e profundidade iterativa para comparar os resultados.

Ao final, você deverá entregar três tabelas preenchidas, uma para cada algoritmo, e com a seguinte estrutura: 

| Combinação Final | Profundidade da Solução | Tempo de Execução (s) | Uso de Memória (MiB) |
| ---------------- | ----------------------- | --------------------- | -------------------- |
| [6, 9]           |         ??              |        ??             |       ??             |

Cada tabela deve ter 19 linhas, da profundidade 0 até a profundidade 18, considerando as combinações finais possíveis para o cadeado.

Ao terminar as três tabelas, faça uma análise comparativa entre os algoritmos, discutindo as vantagens e desvantagens de cada um em relação ao tempo e uso de memória para diferentes profundidades de solução.

??? "Pergunta!"

    Os resultados encontrados tem relação com o que foi visto em aula sobre os algoritmos de busca? 

## Entrega das implementações e do relatório

A implementação da classe `Cadeado2` deve ser entregue em um arquivo chamado `cadeado2.py`. O relatório deve ser entregue no arquivo README.md, contendo as tabelas preenchidas e a análise comparativa entre os algoritmos. Certifique-se de incluir os códigos utilizados para medir o tempo e a memória de execução. 

Todos os artefatos devem ser organizados em um repositório no GitHub [https://classroom.github.com/a/DTYRGvxr](https://classroom.github.com/a/DTYRGvxr). A data de entrega desta APS é **13/03/2026 até às 13:00 horas**. 

Este projeto pode ser feito em grupos com até 3 pessoas.