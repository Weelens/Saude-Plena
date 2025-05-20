# Saúde Plena 

A Saúde Plena é um sistema web de monitoramento de exercícios físicos com plano semanal personalizado. Desenvolvido com Flask e MySQL, o projeto permite que usuários se cadastrem, façam login e visualizem seus treinos por dia da semana.

##  Funcionalidades

- Login seguro com senha criptografada
- Cadastro de novos usuários
- Inserção de novos exercícios por dia da semana
- Visualização dos treinos com link automático para vídeos no YouTube
- PDFs com dicas de saúde e alimentação
- Calendário dinâmico com destaque do dia atual
- Interface responsiva

## Tecnologias utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- MySQL
- Werkzeug (hash de senhas)

## Como rodar o projeto
### 1. Clone o repositório
```bash
git clone https://github.com/weelens/saude-plena.git
cd saude-plena
```
### 2.
#### configure o ambiente virtual é opcional mas recomendo
```bash
python -m venv venv
venv\Scripts\activate
```
##### Linux/macOs
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.
#### Instale as depenpendecias
```bash
 pip install -r requirements
```

### 4 Configure o banco.
- Certifique-se de que o MySQL está instalado e rodando.
- Crie o banco de dados com o nome `projetos`
- Depois, execute os comandos SQL abaixo para criar as tabelas:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE exercicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    series INT NOT NULL,
    repeticoes INT NOT NULL,
    dia VARCHAR(20) NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES users(id)
);
```

### 5. Ajuste os credencias do seu banco
```py
host='localhost',
user='root',
password='1234',
database='projetos
```
### 6. Excute o app
```bash
python app.py
```

# Autor
- Desenvolvido por Weelens (@Willis)