import pandas as pd

df = pd.read_csv('D:\PYTHON\LEITURA PDF\email.csv')

dfcolunas = df[["Display Name"]]
df.head(None)

#df=df.sort_values(by=['User Principal Name'],ascending=True)

#LENDO COLUNAS EXPECIFICAS 

linhas=df.loc[0:]

print("TESTE DE IMPRESSÃO DAS LOCALIZAÇÕES ",linhas)

#print(dfcolunas)
print("TESTE DE IMPRESSÃO DAS COLUNAS",dfcolunas[2:])

#Obtenha uma lista com os valores exclusivos de uma coluna: você pode usar o método unique() Exemplo abaixo:
print('\n',"Imprimir valores unicos de uma linha:  "'\n\n',df["Display Name"].unique())

#Obtenha o número de linhas e colunas: você pode usar o método shape
print(f"o número de linhas e colunas no total são: "'\n',df.shape)

#Obter o número de linhas: você pode usar o método shape e acessar o primeiro elemento para obter o número de linhas.
print('\n\n',f"O numero de linhas encontradas são: ",df.shape[0])

#Teste de  FOR com a estrtura do indice
for i in range(15):
    print(i)
    print(df["Display Name"][i])
    
print("fim")

