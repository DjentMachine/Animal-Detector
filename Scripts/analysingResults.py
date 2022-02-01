"""
Created on Sat May  8 21:38:55 2021

@author: DBarros
"""

import csv
import os
import pandas as pd

#Loading file
os.chdir("")
imageDB = pd.read_excel("imageDB_AbrilMaio.xlsx")

#Getting false positives, negatives and overall model accuracy    
falseNega = 0
falsePosi = 0
trueNega = 0
truePosi = 0
correct = 0
for i in range(len(finalData["Imagem"])):
    if int(finalData["Results"][i]) == int(finalData["Pred"][i]):
        correct += 1
        if int(finalData["Results"][i]) == 1:
            truePosi += 1
        else:
            trueNega +=1    
    elif int(finalData["Results"][i]) == 0 and int(finalData["Pred"][i]) != 0:  
        falsePosi += 1
    elif int(finalData["Results"][i]) == 1 and int(finalData["Pred"][i]) != 1:  
        falseNega += 1

#Estatísticas
print("Falsos positivos: %d" % falsePosi)
print("Falsos negativos: %d" % falseNega)
print("Animais correctamente identificados: %d" %truePosi)
print("Negativos correctamente identificados: %d" %trueNega)
print("Precisão total obtida: %0.3f" %(correct/len(finalData["Imagem"])))
print("Precisão de positivos obtida: %0.3f" %(correct/len(finalData["Imagem"])))


