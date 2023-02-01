---
title: Introdução à Inteligência Artificial
subtitle: Fevereiro de 2023
author: Fabrício Barth 
institute: Inteligência Artificial e Robótica
date: 02/2023
theme: insper
aspectratio: 169
...

# Um pouco de Ficção

## O que são? O que fazem? Como fazem? 

\begin{figure}
\centering
\includegraphics[width=0.7\textwidth]{figuras/r2d2.jpg}
\caption{R2D2 e C3PO em Star Wars}
\end{figure}

## E este aqui? Qual é a diferença?

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{figuras/hal9000.jpg}
\caption{HAL 9000 em 2001: A Space Odyssey}
\end{figure}

## E este aqui? Alguém já viu?

\begin{figure}
\centering
\includegraphics[width=0.75\textwidth]{figuras/carbon.png}
\caption{AI em Altered Carbon}
\end{figure}

## O que este tem de diferente dos demais?

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{figuras/ai_film.jpg}
\caption{AI movie}
\end{figure}

## E estes?

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{figuras/smith_matrix.jpeg}
\caption{Agente Smith e outros em Matrix}
\end{figure}

## Resumo

* Vamos sumarizar o que este exemplos da **ficção científica são**, 
  * o **que** eles fazem, 
  * **como** eles fazem e
  * **onde** eles atuam? 

# Será que a ficção tem relação com a ciência?

## 1950 Turing's "Computing Machinery and Intelligence" 

The Imitation Game: "Can machines think?"

![Turing's paper](figuras/turing.jpg)

## 1956 Dartmouth meeting "Artificial Intelligence" adopted

\begin{center}
\includegraphics[width=0.7\textwidth]{figuras/dartmouth.png}
\end{center}

## Objetivos da IA

**Teórico**: a criação de teorias e modelos para a
  capacidade cognitiva. Compreender o que é inteligência e como o
  raciocínio se processa.

  \vspace{1cm}

**Prático**: $\cdots$

# Um pouco de realidade

## Atividade em grupo (1/3)

* Formem grupos de 5 estudantes. 
* Cada grupo deve escolher um dos setores abaixo: 
  * Saúde
  * Educação
  * Segurança
  * Financeiro
  * Transportes
  * E-commerce
  * Agronegócio
  * Cinema e Publicidade

## Atividades em grupo (2/3)

* Cada grupo deve fornecer 2 exemplos de aplicações que fazem uso de Inteligência Artificial e 2 exemplos de aplicações que não fazem uso de Inteligência Artificial considerando o setor escolhido.

* Cada grupo deve justificar os exemplos escolhidos. Descrever o motivo de uma aplicação estar categoriza como aplicação de IA ou não.

* Cada grupo deve criar um arquivo PPT com imagens das aplicações escolhidas, títulos para as aplicações escolhidas justificativa para os exemplos escolhidos e referências onde podem ser encontradas mais informações sobre as aplicações selecionadas. 

## Atividades em grupo (3/3)

* Cada grupo deve enviar o arquivo para o email fabriciojb at insper dot edu dot br.

* Na próxima aula cada grupo terá 10 minutos para apresentar o seu trabalho. 

## Para aqueles que já terminaram

* Pergunte para o [ChatGPT](https://chat.openai.com/):
  * "What is General AI?"
  * "O que é um agente autônomo?"

* Compare a resposta dada pelo ChatGPT com o conteúdo que está nos Verbetes da Wikipedia sobre:
  * "artificial general intelligence"  
  * "autonomous agent".

* Por favor, faça isto em sala de aula ou até a próxima aula.  


<!--

# Exemplos de Aplicações de IA

## IBM Deep Blue vence Kasparov (1997)

\begin{center}
\includegraphics[width=0.6\textwidth]{figuras/deep_blue.jpg}
\end{center}

## Criação do Dataset MNIST (1998)

:::::::::::::: {.columns}
::: {.column width="50%"}
\includegraphics[width=1\textwidth]{figuras/mnist.jpeg}
:::
::: {.column width="50%"}
The MNIST database of handwritten digits

\vspace{0.5cm}

```{.python}
from keras.datasets import mnist
(train_X, train_y), 
(test_X, test_y) = mnist.load_data()
```

\vspace{0.5cm}

Em 2012 existe uma solução que tem erro de teste igual a 0.23% [[http://yann.lecun.com/exdb/mnist/]](http://yann.lecun.com/exdb/mnist/)

:::
::::::::::::::

## Veículos autônomos 

A equipe de Stanford ganha a competição da DARPA no deserto (2005)

\begin{center}
\includegraphics[width=0.6\textwidth]{figuras/car_stanford.jpg}
\end{center}

## Criação do Dataset ImagineNet (2009) 

:::::::::::::: {.columns}
::: {.column width="50%"}
\includegraphics[width=1\textwidth]{figuras/image_classification.png}
:::
::: {.column width="50%"}

Este dataset possui 14.197.122 imagens anotadas de acordo com a taxonomia da WordNet. Desde 2010 este dataset é usado na competição *ImageNet Large Scale Visual Recognition Challenge* (ILSVRC) e é um benchmark clássico para **classificação de imagens** e **reconhecimento de objetos**.

:::
::::::::::::::

## IBM Watson vence no Jeopardy (2011)

\begin{center}
\includegraphics[width=0.5\textwidth]{figuras/watson.jpg}
\end{center}

A partir de **2015** proliferação de **assistentes virtuais** que fazem uso de **classificação de texto** para compreensão das intenção de uma sentença.

## AlphaGO e AlphaGO Zero vencem no GO (2016)

:::::::::::::: {.columns}
::: {.column width="50%"}
\includegraphics[width=0.8\textwidth]{figuras/alphago.png}
:::
::: {.column width="50%"}
\includegraphics[width=1\textwidth]{figuras/go.jpg}
:::
::::::::::::::

# O que existe de comum nestes exemplos?

## O que existe de comum nestes exemplos?

* Todos têm um objetivo bem claro. Uma função de utilidade muito bem definida. 

* Todos estão inseridos em um ambiente muito bem controlado, exceto o veículo autônomo 
(questionável no caso da competição). 

* Todos podem ser vistos como agentes orientados a meta. 

<!-- ## Desafios

* Less data

* Fairness

* Truth

-->

<!--
# O que é um agente orientado a meta ou agente autônomo?
-->