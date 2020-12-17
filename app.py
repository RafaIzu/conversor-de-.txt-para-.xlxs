import pandas as pd
import numpy as np
import re

arquivo = open('input/EXEMPLO_ARQUIVO.txt', 'r')
dicionario = {'id':[], 'nome':[], 'codigo1':[], 'endereco':[],'codigo2':[], 'codigo3':[] }
dados = arquivo.readlines()

for i in range(len(dados)):
    amostra = dados[i].replace(" ","")
    primeiro_dado = amostra[:20]
    dicionario['id'].append(primeiro_dado)
    amostra = amostra.replace(primeiro_dado,"")
    segundo_dado = re.findall("\D{3,}", dados[i])[0].strip()
    dicionario['nome'].append(segundo_dado)
    remover = segundo_dado.replace(" ","")
    amostra = amostra.replace(remover,"")
    terceiro_dado = amostra[:10]
    dicionario['codigo1'].append(terceiro_dado)
    amostra = amostra.replace(terceiro_dado,"")
    quarto_dado = re.findall("\D{3,}", dados[i])[1].strip()
    dicionario['endereco'].append(quarto_dado)
    remover = quarto_dado.replace(" ","")
    amostra=amostra.replace(remover,"")
    quinto_dado= amostra[:2]
    dicionario['codigo2'].append(quinto_dado)
    ultimo_dado = amostra.replace(quinto_dado,"")[:1]
    dicionario['codigo3'].append(ultimo_dado)


tabela_final = pd.DataFrame.from_dict(dicionario)

print(tabela_final)

tabela_final.to_excel('output/tabela_final.xlsx', index=False)

# se você quiser em formato csv descomente o código abaixo
#tabela_final.to_excel('tabela_final.csv', index=False)

arquivo.close()