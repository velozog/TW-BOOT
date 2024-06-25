import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import random, randint
import os
import pywhatkit as kit

PATH = os.path.dirname(__file__)


NUMERO_TELEFONE = "+5548996341504"
colorama.init(autoreset=True)
TEXTO = colored("TW BOOT", "green")
CAMINHO_IMAGEM = os.path.join(PATH, "imagens/tropas_insuficiente.png")
iniciar = input(colored("Se estiver tudo certo, Digite Enter para iniciar: ", "cyan"))
print(colored(f"Inicializando {TEXTO}\n", "cyan"))
pg.PAUSE = 0.5
sleep(3)


def enviar_mensagem_whatsapp(numero, mensagem) -> bool:
    try:
        kit.sendwhatmsg_instantly(numero, mensagem)
        print(f"Mensagem enviada para {numero} com sucesso.")
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao enviar a mensagem: {e}")
        return False


def manda_msg(mensagem):
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    repet = 0
    while not enviar_mensagem_whatsapp(NUMERO_TELEFONE, mensagem) or repet == 3:
        sleep(10)
        repet += 1
    pg.hotkey("alt", "f4")
    sleep(3)
    pg.press("enter")
        
            

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
                pg.click(img.x, img.y)
            if img2:
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
    sleep(3)
    return "Atualizando a pagina"


def proxima_execucao(tempo):
    data_hora_atual = datetime.now()
    data_hora_futura = data_hora_atual + timedelta(minutes=tempo)
    colored(print(f"Vamos aguardar {tempo} minutos"), "yellow")
    return f"Proxima Execução {data_hora_futura.strftime("%d/%m/%Y %H:%M")}"


def main():
    while True:
        
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

        tempo = randint(30, 40)
        msg_inicio = f"Script iniciando {data_hora_atual}"
        mensagem = f"Script funcionando corretamente, finalizado as {data_hora_atual}, {proxima_execucao(tempo)}"
        print(colored(manda_msg(msg_inicio), "green"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("2"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("3"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("4"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("1"), "yellow"))
        print(colored(proxima_execucao(tempo), "cyan"))
        print(colored(manda_msg(mensagem), "green"))
        print(colored(pause_tempo(tempo), "light_yellow", on_color="on_dark_grey"))


if __name__ == "__main__":
    main()
