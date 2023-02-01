# Inteligência Artificial e Robótica

Este projeto possui o material da disciplina de Inteligência Artificial e Robótica ministrada para o BCC.

## Setup do ambiente

Configurando um ambiente virtual:

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

## Executando o servidor localmente

```bash
mkdocs serve
```

## Publicar nova versão da página web

Para publicar o novo conteúdo da página web basta fazer um `push` para o branch gh-pages e executar: 

````bash
mkdocs gh-deploy
````

## Compilando material escrito em Markdown

Segue um exemplo sobre como compilar os materiais que estão em markdown: 

````bash
pandoc -t beamer slides.md -o slides.pdf
````

## Atualizando plano de aula

Para atualizar o plano de aula no site basta digitar: 

````bash
python publica-plano-de-aulas.py
````





