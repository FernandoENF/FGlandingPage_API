## API para landing page da FG

É uma api para uma landing page da Fábrica de Gênios com o propósito de captar dados do formulário de inscrição.

## Tecnologias

A tecnologia utilizada foi o Django, com as seguintes depêndencias:

* Django	3.2.5
* asgiref	3.4.1
* click	8.0.1
* colorama	0.4.4
* django-cors-headers	3.7.0
* djangorestframework	3.12.4
* mysqlclient	2.0.3
* pip	21.1.3
* pytz	2021.1
* setuptools	57.2.0
* sqlparse	0.4.1

## Introdução

* Instale as dependências no seu interpretador Python
* Para rodar a aplicação, vá no diretório do seu projeto e use o comando:
>    python manage.py runserver

## Como utilizar

A aplicação conta com duas rotas:

  - {domain}/api/alunos/
  - {domain}/admin

Para utilizar a API você faz requisições GET e POST na rota "/api/alunos/".
O POST deve ser feito com os seguintes campos:
{
  "name":
  "email":
  "telephone":
  "ref_code":
}
Todos os campos são obrigatórios, porém no ref_code é possível passar um valor nulo.

Para o gerenciamento administrativo basta acessar a rota "/admin" normalmente e utilizar as credenciais de superusuário.

## Funcionalidades

  * Rota "api/alunos/"
    - Retorna um JSON com todos os alunos cadastrados (GET)
    - Cadastra um novo aluno, é possível indicar se alguém foi recomendado ao passar o código no campo ref_code (POST)
  * Rota "/admin"
    - Gerenciamento administrativo 

## Versionamento

1.0.0.0


## Autores

* **Fernando Eulálio**: @FernandoENF (https://github.com/FernandoENF)


