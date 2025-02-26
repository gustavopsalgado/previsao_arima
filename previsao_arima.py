import pandas as pd
import matplotlib.pyplot as plt

arquivo_excel = 'planilha.xlsx'
planilhas = ['AAPL', 'PETR4 SA', 'VISC11 SA'] 

coluna_precos = 'Preço de Fechamento Ajustado2' 

dados_historicos = {}

for planilha in planilhas:
    
    df = pd.read_excel(arquivo_excel, sheet_name=planilha)

    print(f'\nDados da planilha {planilha}:')
    print(df.head())

  
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce') 
    df.set_index('Data', inplace=True)

    df = df.dropna()

    if df.empty:
        print(f"A planilha {planilha} está vazia ou contém dados inválidos.")
        continue

    if coluna_precos not in df.columns:
        print(f"A coluna '{coluna_precos}' não foi encontrada na planilha {planilha}.")
        continue

    df_precos = df[[coluna_precos]]

    dados_historicos[planilha] = df_precos[-(5*52):]  # 5 anos de dados semanais

if dados_historicos:
    
    plt.figure(figsize=(12, 6))

    for planilha in planilhas:
        df_historico = dados_historicos[planilha]
        plt.plot(df_historico.index, df_historico[coluna_precos], label=f'Dados Históricos {planilha}')

    plt.title('Dados Históricos (5 anos) para AAPL, PETR4 SA e VISC11 SA')
    plt.xlabel('Data')
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)

    plt.show()