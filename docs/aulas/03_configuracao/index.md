# Implementando um Aspirador de Pó

## Configuração do ambiente

Para executar esta atividade você terá que instalar a biblioteca [AIGYM](https://pypi.org/project/aigyminsper/):

```bash
pip install aigyminsper
```

Recomenda-se fortemente que todo estudante faça estas atividades em sua máquina. Os problemas podem ser discutidos em grupo, no entanto, cada aluno precisa ter a sua própria implementação. 

Nas pastas `aigyminsper` e `tests` do projeto [AIGYM](https://github.com/Insper/ai_gym) você irá encontrar diversos arquivos `python`. São os arquivos desta pasta que você irá utilizar neste exercício.

## Exercício: Aspirador de Pó 

Na pasta `tests` temos o arquivo `ProblemSpecificationExample.py`. 

* Faça uma cópia deste arquivo e chama ele de `AspiradorPo.py`, por exemplo.
* No método `__init__` defina a estrutura de dados que você especificou na aula passada. 
* No método `sucessors` codifique a execução das ações segundo o que você especificou na aula passada. **Dica**: cada novo estado é uma instância de um novo objeto da classe que é adicionado na lista retornada pelo método. 
* Codifique o comportamento do método `is_goal`. Ele deve retornar `True` quando encontrar um estado igual a meta. 
* O médoto `description` retorna uma descrição do problema que está sendo resolvido. Por favor, altere o que está descrito no método. 
* Faça um retorno para o método `env`. Peça para o professor explicar em sala de aula.
* Altere o método `main()` para que o mesmo chame a sua classe. 

??? warning "Conceitos que devem ser explorados neste exercício"

    Representação de um problema na forma de **estado**, **transição**, **grafo**

??? warning "Conceitos que devem ser explorados neste exercício"

    Algoritmos de Busca, começando com o algoritmo de busca em largura. 

## Exercício 2: Aspirador de Pó com 4 quartos.

Vamos implementar um aspirador de pó que atua em um ambiente com 4 quartos? Um quadrado $2 \times 2$? 
