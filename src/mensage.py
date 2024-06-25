import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib


class Whatsapp:
    def __init__(self) -> None:
        self.navegador = None

    def started_autenticate(self) -> None:
        """Iniciar e startar o codigo do whatsapp"""
        self.navegador = webdriver.Chrome()
        self.navegador.get("https://web.whatsapp.com/")
        while len(
            self.navegador.find_element(
                By('//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            )
        ):
            time.sleep(1)

    def get_mensagger(self, menssagger: str, phone_number: str):
        """Enviar mensagem via whattsapp\n
        não enviar muitas mensagem seguidas...


        Args:
            menssagger (str): mensagem a ser enviadas
            phone_number (str): numero a ser enviado a mensagem
        """
        menssagger_ = urllib.parse.quote(menssagger)
        link = f"http://web.whatssap.com/send?phone={phone_number}&text={menssagger_}"
        self.navegador.get(link)
        while len(self.navegador.find_element(By.ID, "side")) < 1:
            time.sleep(1)
        self.navegador.find_element(
            By.XPATH, '//*[@id"main"]/footer/div[1]/div[2]/div/div[2]'
        ).send_keys(Keys.ENTER)
        time.sleep(10)
