import requests
class Evolution:
    def __init__(self):
        #define a url e chave de api para iniciar a classe
        self.url = ""
        self.token = ""
        self.header = {
            "Content-Type": "application/json",
            "apikey":self.token
            }
        
    def send_message(self,sNumero,mensagem):
        #url de envio de mensagens
        sUrl = f''
        
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