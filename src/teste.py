import pyautogui as pg
import time


# def scroll_and_switch_page(scroll_amount, wait_time, max_scroll_attempts):
#     # Definindo o número máximo de tentativas de scroll
#     scroll_attempts = 0

#     while scroll_attempts < max_scroll_attempts:
#         # Tenta dar scroll para baixo
#         pyautogui.scroll(-scroll_amount)
#         time.sleep(wait_time)  # Espera um pouco para a página carregar

#         # Verifica se o scroll teve efeito
#         current_scroll_position = pyautogui.position()
#         pyautogui.scroll(scroll_amount)  # Desfaz o scroll para verificar a posição
#         time.sleep(wait_time)
#         new_scroll_position = pyautogui.position()

#         if new_scroll_position == current_scroll_position:
#             # Se a posição não mudou, muda de página
#             # Aqui você deve adicionar o código para mudar de página
#             print("Mudando de página...")
#             # Por exemplo, você pode clicar em um botão de próxima página
#             # pyautogui.click(x, y)  # Adicione as coordenadas do botão de próxima página
#             scroll_attempts += 1  # Aumenta o número de tentativas de scroll
#         else:
#             # Se a posição mudou, aumenta o número de tentativas de scroll
#             scroll_attempts = 0


# # Defina os parâmetros
# scroll_amount = 100  # Quantidade de scroll para baixo
# wait_time = 2  # Tempo para esperar o carregamento da página
# max_scroll_attempts = (
#     3  # Número máximo de tentativas de scroll antes de mudar de página
# )

# scroll_and_switch_page(scroll_amount, wait_time, max_scroll_attempts)
import os

PATH = os.path.dirname(__file__)
path_img_3 = os.path.join(PATH, "imagens/aint_boot.png")
while True:
    try:
        img3 = pg.locateCenterOnScreen(image=path_img_3)
        if img3:
            pg.click(img3.x, img3.y)
            print("Fudeu anti Boot na area")
            break
    except pg.ImageNotFoundException:
        print("Procurando")
