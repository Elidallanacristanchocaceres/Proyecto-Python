import json
import os

MY_DATABASE = 'data/pacientes.json'

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(MY_DATABASE,'w') as fw:
        json.dump(param[0],fw,indent=4)

def AddData(*param):
    data = list(param)
    with open(MY_DATABASE,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})

        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def ReadFile():
    try:
        with open(MY_DATABASE, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("El archive no existe.")
        return {}  
    except json.decoder.JSONDecodeError:
        print("El archivo se encuentra vacido, no es un formato valido.")
        return {} 
    
def ActualizarArchivo(data):
    with open("data/pacientes.json", "w") as file:
        json.dump(data, file)
    
    
def checkFile(*param):
    data = list(param)
    if not os.path.isfile(MY_DATABASE):
        if len(param):
            NewFile(data[0])
    else:
        if len(param):
            data[0].update(ReadFile())



