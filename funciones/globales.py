from os import system
import sys 
from enum import Enum

def borrar_pantalla():
    if sys.platform =="linux" or sys.platform == "dawin":
        system('clear')
    else:
        system('cls')

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "dawin":
        x=input("Oprima una tecla para continuar :")
    else:
        system("pause")

centroMedico = {
    "data": {}
}