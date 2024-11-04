# Chatbot Interativo

Este é um chatbot interativo desenvolvido com **Streamlit**, **Langchain** e **LangGraph**. A aplicação utiliza um modelo de linguagem (LLM) da Groq e armazena informações relevantes em um banco de dados vetorial (FAISS) executado em um container Docker.

## Funcionalidades

- Respostas dinâmicas baseadas nas entradas do usuário.
- Armazenamento de informações relevantes em um banco de dados vetorial.
- Interface simples e interativa usando Streamlit.

## Tecnologias Usadas

- **Streamlit**: Para a criação da interface do usuário.
- **Langchain**: Para a construção da lógica do chatbot.
- **LangGraph**: Para integração de recursos de aprendizado.
- **OpenAI**: Para utilizar um modelo de linguagem.
- **FAISS**: Para armazenamento vetorial, utilizado como banco de dados.
- **Docker**: Para gerenciar a execução do banco de dados.

## Requisitos

- Python 3.7 ou superior
- Docker
### Estrutura do Projeto

```
chatbot/
│
├── app.py
├── requirements.txt
├── docker-compose.yml
└── .env.exemple

```


## Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/chatbot.git
cd chatbot
```

### 2. Crie um ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Configuração do Docker

Crie e inicie o container Docker para o banco de dados vetorial:

```bash
docker-compose up -d
```

### 4. Configuração das Variáveis de Ambiente

Copie o aquivo `.env.exemple` e mude para `.env` na raiz do projeto e adicione sua chave da API:

```
LLM_API_KEY=
```

### 5. Execute a aplicação Streamlit

```bash
streamlit run app.py
```

### 6. Acesse o Chatbot

Abra o navegador e vá para `http://localhost:8501/`.

## Como Usar

1. Digite sua mensagem na caixa de texto.
2. Clique no botão "Enviar" para receber uma resposta do chatbot.
3. O chatbot irá armazenar informações relevantes conforme as interações.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.


```