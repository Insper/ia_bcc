# Alterando os algoritmos de busca

Nas aulas anteriores implementamos algumas versões do problema do aspirador de pó. Para a atividade de hoje vamos considerar a implementação mais simples, que é a que considera um aspirador de pó em um ambiente com 2 quartos. 

## Completando o método `env`

Nesta implementação você vai adicionar o seguinte comportamento no médoto `env()`: 

```python
def env(self):
    return json.dumps(self.__dict__)
```

## Alterando a chamada do método `search`

Na hora de chamar o método `search` altere o código de: 

```python
    algorithm = BuscaLargura()
    result = algorithm.search(state)
```

para: 

```python
    algorithm = BuscaLargura()
    result = algorithm.search(state, trace=True)
```

adicionando o parâmetro `trace=True`. Tente entender o que acontece: (i) qual o resultado encontrado, (ii) qual o conteúdo do log impresso. 

## Alterando o algoritmo de busca

Depois disto, altere o código de: 

```python
    algorithm = BuscaLargura()
    result = algorithm.search(state, trace=True)
```

para:

```python
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, trace=True, m=10)
```

Tente entender o que acontece: (i) qual o resultado encontrado, (ii) qual o conteúdo do log impresso. Por que os resultados são diferentes? 