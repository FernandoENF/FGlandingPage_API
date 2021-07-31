## API para landing page da FG

É uma api para uma landing page da Fábrica de Gênios com o propósito de captar dados do formulário de inscrição.

## Tecnologias

A tecnologia utilizada foi o Django, com as seguintes depêndencias:

* Ruby version  x.x.x
* Rails version x.x.x
* ...

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


