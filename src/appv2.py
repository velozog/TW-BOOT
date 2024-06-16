import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, randint
import os

PATH = os.path.dirname(__file__)
print(PATH)


colorama.init(autoreset=True)
TEXTO = colored("TW BOOT", "green")
CAMINHO_IMAGEM = os.path.join(PATH, "imagens/tropas_insuficiente.png")
iniciar = input(colored("Se estiver tudo certo, Digite Enter para iniciar: ", "cyan"))
print(colored(f"Inicializando {TEXTO}\n", "cyan"))

sleep(3)


def atualizar_pagina():
    while True:
        numero = random.randint(0, 100)
        if numero == 22:
            pg.press("f5")

            return "Atualizando a pagina"


def mandar_tropasv2():
    path_img_1 = os.path.join(PATH, "imagens/botao_1.png")
    path_img_2 = os.path.join(PATH, "imagens/botao_2.png")
    pg.click(x=900, y=630)
    pg.scroll(-500)
    while True:
        try:
            img = pg.locateCenterOnScreen(image=path_img_1)
            img2 = pg.locateCenterOnScreen(image=path_img_2)
            if img:
                sleep(0.8)
                pg.click(img.x, img.y)
            # print(colored(atualizar_pagina(), "green"))
            if img2:
                sleep(0.8)
                pg.click(img2.x, img2.y)

        except pg.ImageNotFoundException as err:
            print(f"Procurando {err}")
        try:
            if pg.locateCenterOnScreen(image=CAMINHO_IMAGEM):
                return colored("Tropas insuficiente", "red")

        except:
            print(colored("Tropas enviadas com sucesso!!", "green"))


def trocar_aldeia(num_aldeia: str):
    if num_aldeia == "1":
        pg.press(num_aldeia)
        return "Retormando a aldeia inicial"
    pg.press(num_aldeia)
    sleep(1)

    return "Indo até a proxima aldeia"


def pause_tempo(tempo):
    sleep(tempo * 60)
    pg.click(x=900, y=630)
    pg.press("f5")
    return "Atualizando a pagina"


def proxima_execucao(tempo):
    data_hora_atual = datetime.now()
    data_hora_futura = data_hora_atual + timedelta(minutes=tempo)
    colored(print(f"Vamos aguardar {tempo} minutos"), "yellow")
    return f"Proxima Execução {data_hora_futura}"


def main():
    while True:
        tempo = randint(25, 35)

        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("2"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("3"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("1"), "yellow"))
        print(colored(proxima_execucao(tempo), "cyan"))
        print(colored(pause_tempo(tempo), "light_yellow", on_color="on_dark_grey"))


if __name__ == "__main__":
    main()
