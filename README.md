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

Para publicar o novo conteúdo da página web basta executar: 

````bash
mkdocs gh-deploy
````

No entanto, se fizer isto, todo o conteúdo que está local, mesmo se não exister no `main`, será publicado em gh-pages. 
Para que isto não aconteça, este projeto tem um script em `.github/workflows/main.yml` que define uma action para publicação em `gh-pages` a partir do `main`.

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





