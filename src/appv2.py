import pyautogui as pg
from time import sleep, time
from datetime import datetime, timedelta
from termcolor import colored
import colorama
from random import randint
import os
import pywhatkit as kit

PATH = os.path.dirname(__file__)


NUMERO_TELEFONE = "+5548996341504"
colorama.init(autoreset=True)
TEXTO = colored("TW BOOT", "green")
CAMINHO_IMAGEM = os.path.join(PATH, "imagens/tropas_insuficiente.png")
print(colored(f"Inicializando {TEXTO}\n", "cyan"))

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
    sleep(2)
    pg.hotkey("alt", "f4")
    sleep(1)
    pg.press("enter")
        
            

def mandar_tropasv2():
    path_img_1 = os.path.join(PATH, "imagens/botao_1.png")
    path_img_2 = os.path.join(PATH, "imagens/botao_2.png")
    path_img_3 = os.path.join(PATH, "imagens/aint_boot.png.png")
    pg.click(x=900, y=630)
    sleep(1)
    pg.scroll(-500)
    sleep(0.5)

    while True:
        try:
            img = pg.locateCenterOnScreen(image=path_img_1)
            img2 = pg.locateCenterOnScreen(image=path_img_2)
            img3 = pg.locateCenterOnScreen(image=path_img_3)
            if img:
                # sleep(0.2)
                pg.click(img.x, img.y)
                print(colored("Tropas enviadas com sucesso!!", "green"))
            else:
                # sleep(0.2)
                pg.click(img2.x, img2.y)
                print(colored("Tropas enviadas com sucesso!!", "green"))

        except pg.ImageNotFoundException as err:
            print(f"Procurando {err}")
            pg.scroll(-300)
        try:
            if pg.locateCenterOnScreen(image=CAMINHO_IMAGEM):
                return colored("Tropas insuficiente", "red")
           

        except:
            print(colored("Ainda tem tropas na aldeia", "green"))


def trocar_aldeia(num_aldeia: str):
    if num_aldeia == "1":
        pg.press(num_aldeia)
        return "Retormando a aldeia inicial"
    pg.press(num_aldeia)
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
        tempo = randint(20, 25)
        msg_inicio = f"{TEXTO} iniciado em {data_hora_atual}"
        print(colored(msg_inicio, "blue"))
        # print(colored(manda_msg(msg_inicio), "green"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("2"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("3"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("4"), "yellow"))
        print(colored(mandar_tropasv2(), "red"))
        print(colored(trocar_aldeia("1"), "yellow"))
        data_hora_atual2 = datetime.now().strftime("%d/%m/%Y %H:%M")
        mensagem = f"Script funcionando corretamente, finalizado em {data_hora_atual2}, {proxima_execucao(tempo) } "
        print(colored(mensagem, "cyan"))
        # print(colored(manda_msg(mensagem), "green"))
        print(colored(pause_tempo(tempo), "light_yellow", on_color="on_dark_grey"))


if __name__ == "__main__":
    main()
