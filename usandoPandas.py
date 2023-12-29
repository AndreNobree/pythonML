import pandas as pd 

lerExcel = pd.read_excel('CRE_Equipamentos3.xlsx')

#"head()" mostra as primeira 5 linhas do arquivo
cabecalho = lerExcel.head()

print(cabecalho)

lerCSV = pd.read_csv('Contas a serem pagas.csv')

#eu posso especificar o tanto de linhas
cabecalho2 = lerCSV.head(10)
print(cabecalho2)

#le todas as linhas do arquivo
print(lerCSV)