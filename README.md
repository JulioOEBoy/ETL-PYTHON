# Projeto ETL com Python

Este projeto demonstra o fluxo **ETL (Extract, Transform, Load)** utilizando Python e Pandas.  
O objetivo é extrair dados de usuários, transformá-los em mensagens personalizadas e carregar os resultados em um novo arquivo CSV.

## 🚀 Fluxo ETL
- **Extração**: leitura de dados fictícios de um arquivo CSV (`usuarios.csv`).
- **Transformação**: geração de mensagens personalizadas para cada usuário.
- **Carregamento**: salvamento das mensagens em um novo arquivo (`mensagens.csv`).

## 📂 Estrutura
- `etl.py`: script principal com as etapas ETL.
- `usuarios.csv`: dados fictícios de entrada.
- `mensagens.csv`: arquivo gerado com as mensagens personalizadas.
- `README.md`: documentação do projeto.

## ▶️ Como Executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
