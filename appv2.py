import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, randint



colorama.init(autoreset=True)
TEXTO = "TW BOOT"
CAMINHO_IMAGEM = r"C:\Users\Geziel Velozo\Documents\Sem título.png"
iniciar = input("Se estiver tudo certo, Digite Enter para iniciar: ")
print(colored(f"Inicializando {TEXTO}", "cyan"))
sleep(2)

def mandar_tropas():
    while True:
        tempo = random()
        x = randint(935, 952)
        y = randint(694, 705)
        sleep(tempo)
        pg.click(x=x, y=y)
        print(colored("Tropas enviadas com sucesso!!", "green"))
        try:
            if pg.locateCenterOnScreen(CAMINHO_IMAGEM):
                print(
                    colored(
                        "Tropas Insufuciente, esperando o retorno pra continuar.",
                        "red",
                    )
                )
                print(
                    colored(
                        "tropas dessa aladeia insficiente, indo ate a proxima aldeia!", "yellow"
                    )
                )
                return
        except:
            print(colored("quantidade de tropas suficiente!", "green"))

def trocar_aldeia():
    pg.click(x=304, y=251)
    sleep(1)
    pg.click(x=304, y=251)

def voltar_aldeia_inicial():
    pg.click(x=284, y=250)
    sleep(1)
    pg.click(x=284, y=250)

def pause_tempo(tempo):
    sleep(tempo*60)
    pg.click(x=900, y=630)
    print(colored("Atualizando a pagina", "green"))
    pg.press("f5")
    sleep(5)

def proxima_execucao(tempo):
    data_hora_atual = datetime.now()
    data_hora_futura = data_hora_atual + timedelta(minutes=tempo)
    print(colored(f"Vamos aguardar {tempo} minutos"))
    print(colored(f"Proxima Execução {data_hora_futura}", "cyan"))

def main():
    while True:
        tempo = randint(25, 35)
        mandar_tropas()
        trocar_aldeia()
        mandar_tropas()
        voltar_aldeia_inicial()
        proxima_execucao(tempo)
        pause_tempo(tempo)
if __name__ == "__main__":
    main()
