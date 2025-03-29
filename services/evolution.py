import requests
class Evolution:
    def __init__(self):
        #define a url e chave de api para iniciar a classe
        self.url = "https://k1evolution.vmserverlab.site"
        self.token = "0CEFBB4C8663-4496-897B-7FB2BE02DC5C"
        self.header = {
            "Content-Type": "application/json",
            "apikey":self.token
            }
        
    def send_message(self,sNumero,mensagem):
        #url de envio de mensagens
        sUrl = f'https://k1evolution.vmserverlab.site/message/sendText/Kaua'
        
        #header padrado
        jHeaders = self.header
        
        jBody = {
        "number": sNumero,
        "text": mensagem,
        "delay": 5000,
        }
        if sNumero != '5511964525876':
            response = requests.post(sUrl, json=jBody, headers=jHeaders)
            return response.json()