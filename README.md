
# Projeto "Lista de Atividades"

Este é um projeto **Django** que permite aos usuários gerenciar suas atividades de forma eficiente. O objetivo deste projeto é fornecer uma maneira simples de adicionar, editar e listar tarefas, com um foco em produtividade e organização.

## Funcionalidades

- **Lista de Tarefas**: O usuário pode visualizar todas as tarefas cadastradas.
- **Criação de Tarefas**: É possível adicionar novas tarefas com descrição, prazo e status.
- **Edição de Tarefas**: O usuário pode editar tarefas existentes.
- **Interface Responsiva**: O design do sistema foi feito para ser simples e fácil de usar.

## Tecnologias Utilizadas

- **Django**: Framework web para a criação de APIs e gerenciamento de dados.
- **Python**: Linguagem de programação principal utilizada no desenvolvimento do projeto.
- **HTML/CSS**: Para a criação da interface web.
- **Bootstrap**: Framework para design responsivo.
- **SQLite**: Banco de dados utilizado no desenvolvimento e testes do projeto (pode ser alterado para outro banco de dados conforme necessário).

## Como Rodar o Projeto

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu computador:


git clone https://github.com/seu-usuario/lista-de-atividades.git


### 2. Acesse o Diretório do Projeto

Navegue até a pasta do projeto:


cd lista-de-atividades


### 3. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:


python3 -m venv venv


Ative o ambiente virtual:

- **No Linux/Mac**:
  
  source venv/bin/activate
  

- **No Windows**:
  
  venv\Scriptsctivate
  

### 4. Instalar as Dependências

Instale as dependências necessárias para o projeto utilizando o `pip`:


pip install -r requirements.txt


### 5. Realizar as Migrações

Execute as migrações para criar as tabelas no banco de dados:


python manage.py migrate


### 6. Criar um Superusuário (Opcional)

Se você quiser acessar a área administrativa do Django, crie um superusuário:


python manage.py createsuperuser


Siga as instruções para configurar o superusuário (nome de usuário, e-mail, senha).

### 7. Rodar o Servidor

Por fim, inicie o servidor de desenvolvimento do Django:


python manage.py runserver


O projeto estará disponível em `http://127.0.0.1:8000/` no seu navegador.

---

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, realizar alterações e enviar um pull request. A contribuição é sempre bem-vinda!

1. Fork o repositório.
2. Crie uma nova branch para suas alterações.
3. Faça commit das suas mudanças.
4. Envie um pull request com a descrição do que foi alterado.

---

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Você pode me encontrar nas seguintes plataformas:

- **GitHub**: [https://github.com/hebertlago](https://github.com/hebertlago)
- **LinkedIn**: [https://www.linkedin.com/in/hebert-lago](https://www.linkedin.com/in/hebert-lago)
- **Email**: hebertlagoo@gmail.com