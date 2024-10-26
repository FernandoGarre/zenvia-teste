
# Arquitetura de Dados para Plataforma de Notificações

## Visão Geral

Este projeto processa notificações do WhatsApp para milhares de clientes em tempo real. A arquitetura é composta por três componentes principais:

1. **Kafka Consumer**: Serviço que consome mensagens de notificações em tempo real do tópico Kafka e as armazena em um banco de dados PostgreSQL.
2. **Banco de Dados (PostgreSQL)**: Banco de dados relacional usado para armazenar todas as notificações recebidas para posterior análise e geração de relatórios.
3. **Painel de Notificações (Flask)**: Aplicação web que exibe o número total de notificações recebidas por cliente.
4. **Relatórios Diários**: Scripts que geram relatórios detalhados de notificações e de cobrança diariamente.

## Fluxo de Dados

1. As notificações são enviadas para um tópico Kafka em tempo real.
2. O Kafka Consumer lê as mensagens do tópico e as salva no banco de dados PostgreSQL.
3. O Painel de Notificações acessa o banco de dados para exibir o total de notificações por cliente.
4. Relatórios diários de notificações e de cobrança são gerados a partir dos dados no banco de dados.
