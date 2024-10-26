
# Execução dos Serviços do Projeto Zenvia - Plataforma de Notificações

Este documento fornece todas as instruções necessárias para configurar o ambiente, instalar as dependências e executar cada um dos serviços do projeto de processamento de notificações do WhatsApp.

---

## Requisitos do Projeto

1. **Ferramentas Necessárias**:
   - **Python 3.x**: Linguagem de programação usada para o desenvolvimento dos serviços.
   - **PostgreSQL**: Banco de dados relacional para armazenar as notificações.
   - **Kafka**: Plataforma de streaming de dados usada para consumir notificações em tempo real.

2. **Bibliotecas Python**:
   - `kafka-python`: Para consumir mensagens do Kafka.
   - `psycopg2`: Para conectar e manipular o banco de dados PostgreSQL.
   - `flask`: Para criar uma aplicação web para o painel de notificações.

## Instalação das Dependências

Para instalar as bibliotecas Python necessárias, execute o seguinte comando no terminal:

```bash
pip install kafka-python psycopg2 flask
```

---

## Configuração do Banco de Dados

1. **Crie o Banco de Dados**:
   - Abra o PostgreSQL e crie um banco de dados chamado `notificacoes` com o comando:

     ```sql
     CREATE DATABASE notificacoes;
     ```

2. **Configuração da Tabela**:
   - No banco de dados `notificacoes`, crie a tabela `notificacoes` para armazenar as mensagens consumidas do Kafka. Execute o seguinte comando SQL para criar a tabela:

     ```sql
     CREATE TABLE notificacoes (
         customer_id VARCHAR(20),
         message_id VARCHAR(20),
         customer_name VARCHAR(50),
         payload TEXT,
         event_datetime TIMESTAMP
     );
     ```

3. **Configuração do Usuário do Banco de Dados**:
   - Certifique-se de que o PostgreSQL tenha um usuário com as permissões necessárias para acessar e manipular o banco de dados `notificacoes`. Atualize o script com as credenciais do banco de dados, se necessário.

---

## Configuração do Kafka

1. **Instale e Configure o Kafka**:
   - Baixe e instale o Kafka conforme a documentação oficial (https://kafka.apache.org/quickstart).
   - Inicie o servidor Kafka e crie um tópico chamado `notificacoes`, que será usado para transmitir as mensagens de notificação.

     ```bash
     # Comando para criar o tópico "notificacoes"
     kafka-topics.sh --create --topic notificacoes --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```

---

## Execução dos Serviços

Aqui estão os passos para executar cada um dos serviços do projeto.

### 1. Consumidor Kafka

O serviço do **Kafka Consumer** consome mensagens de um tópico Kafka (`notificacoes`) e as salva no banco de dados PostgreSQL.

- **Localização do Script**: `src/kafka_consumer/consumer.py`
- **Como Executar**:
  
  Execute o seguinte comando no terminal para iniciar o consumidor Kafka:

  ```bash
  python src/kafka_consumer/consumer.py
  ```

- **Descrição**:
  Esse script consome mensagens JSON de notificações do Kafka, extrai os campos e insere cada mensagem no banco de dados PostgreSQL.

---

### 2. Painel de Notificações

O **Painel de Notificações** é uma aplicação web construída com Flask. Ele exibe o total de notificações recebidas por cliente, atualizando os dados a partir do banco de dados.

- **Localização do Script**: `src/notification_panel/app.py`
- **Como Executar**:

  Execute o seguinte comando para iniciar o servidor Flask:

  ```bash
  python src/notification_panel/app.py
  ```

- **Acessar o Painel**:
  Após iniciar o servidor, abra o navegador e acesse o painel de notificações em: `http://localhost:5000`

- **Descrição**:
  O painel exibe uma tabela com o número total de notificações por cliente. Ele busca esses dados diretamente no banco de dados PostgreSQL.

---

### 3. Relatórios de Notificação e Cobrança

O script de **Relatórios de Notificação e Cobrança** gera relatórios diários detalhados das notificações, bem como um relatório de cobrança por cliente.

- **Localização do Script**: `src/billing_report/report.py`
- **Como Executar**:

  Execute o comando abaixo para gerar os relatórios:

  ```bash
  python src/billing_report/report.py
  ```

- **Descrição**:
  Esse script gera:
  - **Relatório Detalhado de Notificações**: Listagem de todas as notificações enviadas para cada cliente.
  - **Relatório de Cobrança Diária**: Calcula o total de notificações por cliente e aplica uma taxa para gerar o valor de cobrança.

---

## Testando o Projeto

Aqui estão algumas dicas para testar cada componente:

1. **Kafka Consumer**:
   - Envie mensagens de teste para o tópico `notificacoes` no Kafka.
   - Verifique se as mensagens são armazenadas no banco de dados PostgreSQL corretamente.

2. **Painel de Notificações**:
   - Acesse o painel em `http://localhost:5000` e verifique se os dados exibidos correspondem às notificações do banco de dados.

3. **Relatórios**:
   - Execute o script de relatórios e verifique os resultados gerados no console ou arquivo, dependendo da implementação.

---

## Observações Finais

- **Ordem de Execução**:
  - Certifique-se de que o PostgreSQL e o Kafka estejam em execução antes de iniciar os scripts do projeto.
  - A ordem recomendada para rodar os scripts é:
    1. **Kafka Consumer**: Para capturar e armazenar dados em tempo real.
    2. **Painel de Notificações**: Para visualizar as notificações processadas.
    3. **Relatórios**: Para gerar o relatório detalhado e o relatório de cobrança diária.

- **Possíveis Erros e Soluções**:
  - **Erro de Conexão com o Banco de Dados**: Verifique se o PostgreSQL está em execução e se as credenciais estão corretas.
  - **Erro de Conexão com o Kafka**: Certifique-se de que o servidor Kafka está em execução e o tópico `notificacoes` foi criado corretamente.
