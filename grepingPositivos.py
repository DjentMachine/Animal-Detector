"""
Created on Wed May 19 16:31:05 2021

Script to copy all positive files from a given folder to another.
Globs images in a specific folder for processing (creating bounding boxes)

@author: DBarros
"""
    
#import glob
import os
import shutil
import pandas as pd

path = "C:/Users/DBarros/OneDrive - Biota, Lda/Armadilhagem"
#Change file and folder below to the corresponding month
dados = "C:/Users/DBarros/OneDrive - Biota, Lda/PRJ078/Dados/dados_camaras_AgostoSetembro.xlsx"
pastaDoMes = "Agosto_Setembro/"
rootPath= "C:/Users/DBarros/OneDrive - Biota, Lda/"
results = pd.read_excel(dados, sheet_name="Dados", index_col=(1))

if not os.path.exists(rootPath + "PRJ078/Positivos/" + pastaDoMes):
           os.makedirs(os.path.dirname(rootPath + "PRJ078/Positivos/" + pastaDoMes))
  
counter=0

for i in results.iloc:
    source = rootPath+i[6][i[6].find("Armadilhagem"):]+"\\"+str(i[3])+".JPG"
    destination = rootPath + "PRJ078/Positivos/" + pastaDoMes + str(counter)+".JPG"
    
    if not os.path.exists(destination):
        try:
            shutil.copy(source,  destination)
            counter+=1
            
        except FileNotFoundError:
            print("\nFile %s NOT FOUND!!!\nSomeone messed up your data base, probably...most likely..." %(str(i[3])+".JPG"))    
            print()
            print(i)
            break
            
        


    
    

        
        

#fileList = glob.glob(path + '**/*.JPG', recursive=True)