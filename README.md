# 🧪 valida-o

Aplicação web em **Python** para validação de dados com interface gráfica, construída com **Flask** e banco de dados SQL.

> 🚧 *O repositório não possui uma descrição oficial, então este README é baseado na estrutura observada.* :contentReference[oaicite:0]{index=0}

---

## 📋 Sumário

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura](#estrutura)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 📌 Sobre

Este projeto é um sistema de validação de dados com interface web. Ele utiliza **Flask** como framework backend e um banco de dados SQL para persistência. Possui rotas que exibem páginas em HTML (na pasta `templates`) e recursos estáticos (na pasta `static`). :contentReference[oaicite:1]{index=1}

---

## 🚀 Funcionalidades

- 🎯 Interface web para entrada de dados
- 📦 Conexão com banco de dados SQL (`banco.sql`)
- 🔗 Organização das rotas e lógica em `app.py`
- 🛠 Scripts de conexão em `conect.py`
- 🖼 Páginas e estilos customizados via `templates` e `static` :contentReference[oaicite:2]{index=2}

---

## 🧰 Tecnologias

O projeto utiliza as seguintes tecnologias:

| Tecnologia | Uso |
|------------|-----|
| Python     | Linguagem principal |
| Flask      | Framework web |
| SQL        | Banco de dados |
| HTML/CSS/JS| Interface com o usuário |
| SQLite/MySQL* | Estrutura do banco (dependendo do `banco.sql`) | :contentReference[oaicite:3]{index=3}

---

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Gustavo-Alve/valida-o.git
   cd valida-o
2. Crie um ambiente virtual Python:

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


🚨 Se não existir requirements.txt, instale manualmente Flask e outras libs:

pip install flask

⚙️ Configuração

Configure o banco de dados:

Importe o arquivo banco.sql no seu gerenciador de SQL preferido (ex: SQLite Browser, DBeaver, MySQL Workbench).

Caso o projeto use SQLite, renomeie o arquivo para database.db ou ajuste a URL de conexão no arquivo conect.py.

Ajuste variáveis de ambiente (se aplicável):

export FLASK_APP=app.py
export FLASK_ENV=development

▶️ Uso

Inicie a aplicação:

flask run


Ou diretamente com Python:

python app.py


Abra o navegador e acesse:

http://localhost:5000


A partir daí, insira os dados que deseja validar e explore as funcionalidades da aplicação.

📦 Estrutura do Projeto
valida-o/
├── .vscode/                # Configurações do VSCode
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
├── templates/              # Templates HTML
├── app.py                  # Aplicação principal Flask
├── conect.py               # Conexão com banco de dados
├── banco.sql               # Script SQL do banco
├── README.md               # Documentação (você está aqui!)
└── … outros arquivos …
