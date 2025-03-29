import requests

def enviarMensagem(number):
    url = "https://k1evolution.vmserverlab.site/message/sendText/Kaua"
    headers = {
            "Content-Type": "application/json",
            "apikey":"0CEFBB4C8663-4496-897B-7FB2BE02DC5C"
            }
    data = {
    "number": number,
    "text": "Ignora, estou testando API",
    "delay": 10000,
    "linkPreview": True,
    "mentionsEveryOne": True
    }
    if number != "5511964525876":
        response = requests.post(url, json=data, headers=headers)
        return response.json()





