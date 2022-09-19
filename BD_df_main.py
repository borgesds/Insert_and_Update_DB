# pip install mysql-connector-python
import pandas as pd

from insertDB import insert_banco
from selectDB import select_dados
from updateDB import update_db


# INITIALIZE
# Ler arquivo
df = pd.read_csv('base/BD_Extrator.csv', sep=";", low_memory=False)

df['Loja'] = df['Loja'].astype(str)
df['Número da ADE'] = df['Número da ADE'].astype(str)

df = df.fillna(0)

# print(df.columns)

df_extra = df[['Loja', 'Nome do Cliente', 'CNPJ/CPF do Cliente',
               'Número da ADE', 'Status da Operação', ' Valor Pagos ']]


for i in range(len(df_extra)):

    if df_extra.loc[i, 'Número da ADE'] == select_dados(df_extra.loc[i, 'Número da ADE']):

        update_db(df_extra.loc[i, 'Status da Operação'],
                  df_extra.loc[i, ' Valor Pagos '],
                  df_extra.loc[i, 'Número da ADE'])

        print('UPDATE!!!')
        print('ADE do arquivo')
        print(df_extra.loc[i, 'Número da ADE'])

        # df_extra.drop(i, axis=0, inplace=True)
    else:
        insert_banco(df_extra.loc[i, 'Loja'],
                     df_extra.loc[i, 'Nome do Cliente'],
                     df_extra.loc[i, 'CNPJ/CPF do Cliente'],
                     df_extra.loc[i, 'Número da ADE'],
                     df_extra.loc[i, 'Status da Operação'],
                     df_extra.loc[i, ' Valor Pagos '])

        print(f'INSERT!!! Index = {i} ⚡️')
        print()
print('💻🔋 UPDATE AND INSERT FINIDHED!!! 🔋💻')
