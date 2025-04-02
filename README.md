# Aula-20-SENAI-py
'Projeto Final'
2. SITUAÇÃO PROBLEMA: FORMULÁRIO DE LEADS PARA UMA AGENCIA DE MARKETING DIGITAL

# Gerenciamento de Leads
https://prairie-heath-fb8.notion.site/AULA-20-Projeto-Final-160f92ea880b47d2aabb686793bea4b7

## Sobre o Projeto
Este projeto é um sistema de gerenciamento de leads desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. O sistema permite a inserção, atualização, deleção e visualização de leads, além de incluir campos para nome, e-mail, telefone, interesse, status e follow-up dos leads.

## Funcionalidades
- **Inserir Lead**: Permite adicionar novos leads ao sistema.
- **Atualizar Lead**: Permite editar informações de leads existentes.
- **Deletar Lead**: Permite remover leads do sistema.
- **Visualizar Leads**: Exibe uma tabela com todos os leads cadastrados.
- **Campo de Follow-up**: Inclui um campo de texto para adicionar informações de acompanhamento dos leads.

## Interface do Usuário
A interface do usuário é organizada da seguinte forma:
- **Wireframe Superior**: Contém espaço para um logo, informações de controle e uma breve explicação do gerenciador.
- **Campos de Entrada**: Inclui campos para nome, e-mail, telefone, interesse, status e follow-up. Campos obrigatórios são marcados com um asterisco (*).
- **Botões de Ação**: Botões para salvar, atualizar e deletar leads, alinhados na lateral direita da interface.
- **Tabela de Leads**: Mostra uma tabela com todos os leads cadastrados, incluindo todas as informações relevantes.

## Como Executar o Projeto
1. **Clone o Repositório**:
    ```bash
    git clone https://github.com/lucasnegrelli/lead-management.git
    cd lead-management
    ```

2. **Instale as Dependências**:
    Este projeto utiliza apenas a biblioteca Tkinter, que é incluída por padrão na instalação do Python. Certifique-se de que você tem o Python instalado na sua máquina (versão 3.x).

3. **Execute o Script**:
    ```bash
    python lead_management.py
    ```

## Estrutura do Projeto
```
lead-management/
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

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
