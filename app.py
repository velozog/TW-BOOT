import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, choice

colorama.init(autoreset=True)
texto = "TW BOOT"
caminho_imagem = r"C:\Users\Geziel Velozo\Documents\Sem título.png"
iniciar = input("Se estiver tudo certo, Digite Enter para iniciar: ")
print(colored(f"Inicializando {texto}", "cyan"))
sleep(2)
lista_y = [
    698,
    696,
    702,
    703,
    696,
    695,
    701,
    705,
    701,
    696,
    694,
    695,
    699,
    701,
    697,
    702,
    704,
    696,
    696,
    697,
]
lista_x = [
    948,
    935,
    946,
    940,
    950,
    941,
    951,
    940,
    938,
    938,
    944,
    950,
    951,
    947,
    943,
    951,
    942,
    938,
    952,
    943,
]
pausa = [1800, 1850, 1500, 1550, 1875, 1900, 1920, 1950, 2000]

while True:
    tempo = random()
    x = choice(lista_x)
    y = choice(lista_y)
    data_hora_atual = datetime.now()
    data_hora_futura = data_hora_atual + timedelta(minutes=choice(pausa) / 60)
    sleep(tempo)
    pg.click(x=x, y=y)
    print(colored("Tropas enviadas com sucesso!!", "green"))
    try:
        if pg.locateCenterOnScreen(caminho_imagem):
            print(
                colored(
                    "Tropas Insufuciente, esperando o retorno pra continuar.",
                    "red",
                )
            )
            print(f"Vamos Esperar {choice(pausa)/60} Minutos")
            print(colored(f"Proxima Execução {data_hora_futura}", "cyan"))
            sleep(choice(pausa))
            pg.click(x=900, y=630)
            print(colored("Atualizando a pagina", "green"))
            pg.press("f5")
            sleep(5)
    except:
        print(colored("quantidade de tropas suficiente!", "green"))
