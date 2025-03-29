from flask import Flask, request, jsonify
from bot.bot import AIbot
from services.evolution import Evolution

app = Flask(__name__)

# Rota para mensagens upsert
@app.route("/webhook/messages-upsert", methods=["POST"])
def messages_upsert():
    try:
        data = request.get_json()  # Captura os dados do webhook
        print("Recebido [MESSAGES_UPSERT]:", data)
        sNumero = data["data"]["key"]["remoteJid"].split("@")
        sMensagem = data["data"]["message"]["conversation"]
        print('numero: ',sNumero)

        evolution = Evolution()
        ai_bot = AIbot()

        
        if not data["data"]["key"]["fromMe"]:
            response = ai_bot.ivoke(question=sMensagem)
            evolution.send_message(sNumero=sNumero[0],mensagem=response)
        
        response = {"status": "success", "message": "Messages Upsert recebido"}
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

# Rota para mensagens update
@app.route("/webhook/messages-update", methods=["POST"])
def messages_update():
    try:
        data = request.get_json()  # Captura os dados do webhook
        print("Recebido [MESSAGES_UPDATE]:", data)
        response = {"status": "success", "message": "Messages Update recebido"}
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

# Rota para mensagens delete
@app.route("/webhook/messages-delete", methods=["POST"])
def messages_delete():
    try:
        data = request.get_json()  # Captura os dados do webhook
        print("Recebido [MESSAGES_DELETE]:", data)
        response = {"status": "success", "message": "Messages Delete recebido"}
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

# Rota para envio de mensagens
@app.route("/webhook/send-message", methods=["POST"])
def send_message():
    try:
        data = request.get_json()  # Captura os dados do webhook
        print("Recebido [SEND_MESSAGE]:", data)
        response = {"status": "success", "message": "Send Message recebido"}
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
