import pandas as pd

arquivo_excel = 'despesas.xlsx'

df = pd.read_excel(arquivo_excel, engine='openpyxl')

df