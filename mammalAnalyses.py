# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:33:14 2021

Script that adds mammals only tab to ImageDB
Helping make sense of models' precision 

@author: DBarros
"""
import pandas as pd
import os
os.chdir("C:\\Users\\DBarros\\OneDrive - Biota, Lda\\PRJ078\\Dados")

#Choose your data
data = pd.read_excel("imageDB_AbrilMaio_Efficient.xlsx")
#data = pd.read_excel("imageDB_AbrilMaio_xception.xlsx")

#Analyses for mammals
for j in range(2):
    results = data[data.columns[3+j]]
    falseNega = 0
    falsePosi = 0
    trueNega = 0
    truePosi = 0
    correct = 0
    for i in range(len(data["Images"])):
        if int(data["Predictions"][i]) == int(results[i]):
            correct += 1
            if int(data["Predictions"][i]) == 1:
                truePosi += 1
            else:
                trueNega +=1    
        elif int(data["Predictions"][i]) == 0 and int(results[i]) != 0:  
            falseNega += 1
        elif int(data["Predictions"][i]) == 1 and int(results[i]) != 1:  
            falsePosi += 1
    #Estatísticas
    print("~ESTATÍSTICAS PARA %s:~" %data.columns[3+j])
    print("Total de fotografias analisado: %d" %len(data["Images"]))
    print("Falsos positivos: %d" % falsePosi)
    print("Falsos negativos: %d" % falseNega)
    print("Animais correctamente identificados: %d" %truePosi)
    print("Negativos correctamente identificados: %d" %trueNega)
    print("Precisão total obtida: %0.3f" %(correct/len(data["Images"])))
    print("Precisão de positivos obtida: %0.3f" %(truePosi/(truePosi+falseNega)))
    print()
