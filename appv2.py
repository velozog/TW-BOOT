import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, choice

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

colorama.init(autoreset=True)
texto = "TW BOOT"
caminho_imagem = r"C:\Users\Geziel Velozo\Documents\Sem título.png"
iniciar = input("Se estiver tudo certo, Digite Enter para iniciar: ")
print(colored(f"Inicializando {texto}", "cyan"))
sleep(2)


def aldeia1():
    while True:
        tempo = random()
        x = choice(lista_x)
        y = choice(lista_y)
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
                print(
                    colored(
                        "tropas dessa aladeia insficiente, indo ate a proxima aldeia!"
                    )
                )
                return
        except:
            print(colored("quantidade de tropas suficiente!", "green"))


def aldeia2():
    x = choice(lista_x)
    y = choice(lista_y)
    pg.PAUSE = 0.5
    pg.click(x=304, y=251)
    sleep(1)
    pg.click(x=304, y=251)
    while True:

        sleep(0.5)
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
                return
        except:
            print(colored("quantidade de tropas suficiente!", "green"))


def main():
    while True:
        data_hora_atual = datetime.now()
        data_hora_futura = data_hora_atual + timedelta(minutes=30)
        aldeia1()
        sleep(2)
        aldeia2()
        pg.click(x=284, y=250)
        sleep(1)
        pg.click(x=284, y=250)
        print(colored(f"Proxima Execução {data_hora_futura}", "cyan"))
        sleep(1800)
        pg.click(x=900, y=630)
        print(colored("Atualizando a pagina", "green"))
        pg.press("f5")
        sleep(5)


if __name__ == "__main__":
    main()
