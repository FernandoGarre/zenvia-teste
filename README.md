
# Solução de Processamento de Notificações WhatsApp

Esta solução processa notificações do WhatsApp para uma plataforma de comunicação que utiliza Kafka como fonte de dados, exibe um painel de notificações, gera relatórios detalhados e produz relatórios de cobrança diários.

## Estrutura do Projeto

1. **Ingestão de Dados (Kafka Consumer)**: Consumidor Kafka que lê notificações e as armazena em um banco de dados PostgreSQL.
2. **Painel de Notificações (Flask)**: Interface web que exibe o total de notificações por cliente.
3. **Relatórios Diários**: Scripts que geram relatórios detalhados e de cobrança diária.

## Estrutura de Arquivos e Pastas

- `src/kafka_consumer/consumer.py`: Consumidor Kafka para ingestão de dados.
- `src/notification_panel/app.py`: Aplicação Flask para o painel de notificações.
- `src/notification_panel/templates/painel.html`: Template HTML para o painel.
- `src/billing_report/report.py`: Script para gerar relatórios diários.
- `docs/Arquitetura.md`: Descrição da arquitetura do projeto.
- `docs/EXECUTION.md`: Instruções detalhadas de instalação e execução.

## Documentação e Execução

Para instruções detalhadas de instalação, configuração e execução, consulte o arquivo [docs/EXECUTION.md](docs/EXECUTION.md).
