# CRUD de Usuários

## Sobre o Projeto

Este projeto é um sistema de CRUD (Create, Read, Update, Delete) desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. O sistema permite a inserção, atualização, deleção e visualização de usuários, incluindo campos para nome, e-mail e CPF.

## Funcionalidades

- **Inserir Usuário**: Permite adicionar novos usuários ao sistema.
- **Atualizar Usuário**: Permite editar informações de usuários existentes.
- **Deletar Usuário**: Permite remover usuários do sistema.
- **Visualizar Usuários**: Exibe uma tabela com todos os usuários cadastrados.

## Requisitos Funcionais

- **O que o sistema deve fazer**: 
  - Permitir a inserção de novos usuários com nome, e-mail e CPF.
  - Permitir a edição dos dados dos usuários.
  - Permitir a exclusão de usuários.
  - Exibir uma tabela com os usuários cadastrados.
- **Fluxos de Trabalho**:
  - O usuário insere as informações nos campos de texto e clica em "SALVAR" para adicionar um novo usuário.
  - Para atualizar um usuário, o usuário seleciona o usuário na tabela, edita as informações nos campos de texto e clica em "ATUALIZAR".
  - Para deletar um usuário, o usuário seleciona o usuário na tabela e clica em "DELETAR".
  - A tabela exibe todos os usuários cadastrados no banco de dados.
- **Entradas e Saídas**:
  - Entradas: Nome, E-mail, CPF.
  - Saídas: Tabela de usuários com ID, Nome e E-mail.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.
- **Tkinter**: Biblioteca utilizada para criar a interface gráfica.
- **SQLite**: Banco de dados utilizado para armazenar as informações dos usuários.

## Como Executar o Projeto

1. **Clone o Repositório**:
    ```bash
    git clone https://github.com/lucasnegrelli/crud-usuarios.git
    cd crud-usuarios
    ```

2. **Instale as Dependências**:
    Este projeto utiliza apenas a biblioteca Tkinter, que é incluída por padrão na instalação do Python. Certifique-se de que você tem o Python instalado na sua máquina (versão 3.x).

3. **Execute o Script**:
    ```bash
    python lead_management.py
    ```

## Estrutura do Projeto

```
crud-usuarios/
├── lead_management.py
└── README.md
```

- **lead_management.py**: Contém todo o código do sistema de gerenciamento de leads.
- **README.md**: Este arquivo, que contém informações sobre o projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no repositório.

1. Fork o projeto.
2. Crie uma nova branch: `git checkout -b minha-feature`.
3. Faça suas alterações e commit: `git commit -m 'Minha nova feature'`.
4. Envie para a branch: `git push origin minha-feature`.
5. Abra um Pull Request.
