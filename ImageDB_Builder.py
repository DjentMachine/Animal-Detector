a-*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:08:45 2021

Script that builds a image database for comparing model predictions vs reality

@author: DBarros
"""
import csv
import pandas as pd
import os

os.chdir("")
path = ""
data = ""

#CHANGE THESE FOR EVERY MODEL RUN
#newFile = "imageDB_AbrilMaio_Xception.xlsx"
newFile = "imageDB_AbrilMaio_Efficient.xlsx"
#predictions = "./Predictions/XceptionNet_AbrilMaio.csv"
predictions = "./Predictions/EfficientNetB5_AbrilMaio.csv"

#Create the dataframes
results = pd.read_excel(data, sheet_name=3, index_col=(1))
mammals = pd.read_excel(data, sheet_name=4, index_col=(1))
results["Path"] = results["Path"].apply(lambda x:x[len(path):])
mammals["Path"] = mammals["Path"].apply(lambda x:x[len(path):])

#Create a new CSV while using my predictions as a base 
with open(predictions) as predicts:
    preds = csv.reader(predicts)
    imageDB = pd.DataFrame(preds)
    imageDB.columns=["Images","Predictions","Probability"]
    imageDB["Results"] = 0
    imageDB["mammalResults"] = 0
    imageDB["Images"]=imageDB["Images"].apply(lambda x:x[:-4])
    
#Getting the row Results
paths = pd.DataFrame(results["Path"]+"\\"+results["ID_imagem"]) 
mammalPaths = pd.DataFrame(mammals["Path"]+"\\"+mammals["ID_imagem"])
for i in range(len(imageDB)):
    if imageDB["Images"][i] in paths.values:
        imageDB["Results"][i]=1
    if imageDB["Images"][i] in mammalPaths.values:
        imageDB["mammalResults"][i]=1
 
#Saving the file
imageDB.to_excel(newFile, index=False)



        
    
    


    
