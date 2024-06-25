import os
import pywhatkit as kit
import pyautogui as pg
from time import sleep
import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, randint
import os
import pywhatkit as kit


def proxima_execucao(tempo):
    data_hora_atual = datetime.now()
    data_hora_futura = data_hora_atual + timedelta(minutes=tempo)
    colored(print(f"Vamos aguardar {tempo} minutos"), "yellow")
    return f"Proxima Execução {data_hora_futura.strftime("%d/%m/%Y %H:%M")}"


tempo = 30

mensagem = f"Tudo Sub Tranquilo {proxima_execucao(tempo)}"
print(mensagem)
