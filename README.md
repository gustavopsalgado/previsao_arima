# Previsão de Dados Históricos com ARIMA

Este repositório contém um script Python que processa dados históricos de ações e fundos imobiliários a partir de uma planilha do Excel. O script carrega os dados, filtra as informações relevantes e plota um gráfico para análise visual.

## Como funciona

O script `previsao_arima.py` executa as seguintes etapas:

1. **Carregamento dos Dados**: Lê uma planilha Excel especificada no código (`planilha.xlsx`) e extrai os dados de ações e fundos imobiliários listados nas abas `AAPL`, `PETR4 SA` e `VISC11 SA`.
2. **Tratamento dos Dados**:
   - Converte a coluna de datas para o formato correto.
   - Define a coluna de datas como índice.
   - Remove valores ausentes e verifica a existência da coluna de preços (`"Preço de Fechamento Ajustado2"`).
3. **Filtragem Temporal**: Mantém apenas os últimos 5 anos de dados (aproximadamente 260 semanas).
4. **Visualização dos Dados**: Plota um gráfico com as séries temporais das três planilhas, permitindo a análise visual dos dados históricos.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de rodar o script:

```sh
pip install pandas matplotlib openpyxl
```

## Como Executar

1. Coloque a planilha `planilha.xlsx` no mesmo diretório do script.
2. Execute o script Python:

```sh
python previsao_arima.py
```

Se os dados estiverem corretos, um gráfico com os dados históricos das três planilhas será exibido.

## Possíveis Ajustes

- Caso a planilha tenha nomes de abas diferentes, atualize a lista `planilhas` no script.
- Se o nome da coluna de preços for diferente, modifique `coluna_precos`.
- Para considerar um período diferente de 5 anos, ajuste o valor `5*52` na filtragem dos dados.

## Objetivo

Este script facilita a análise de dados históricos para tomadas de decisão em investimentos, fornecendo uma visualização clara da evolução dos ativos ao longo do tempo.

---

