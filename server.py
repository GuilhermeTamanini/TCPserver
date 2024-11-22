from socket import *
from services import decodeprotocol

socketServer = socket(AF_INET, SOCK_STREAM)
listener = ('', 12000)
socketServer.bind(listener)
socketServer.listen(True)

print("Servidor iniciado. Aguardando conexões...")

while True:
    try:
        connection, address = socketServer.accept()
        print(f"Conexão recebida de {address}")

        message = connection.recv(1024).decode()
        print("Mensagem recebida:", message)

        try:
            response = decodeprotocol(message)
            print(response)
            if not response:
                response = "Erro: Comando inválido ou malformado"
        except Exception as e:
            response = f"Erro ao processar a mensagem: {e}"

        connection.send(response.encode())

    except Exception as e:
        print(f"Erro no servidor: {e}")

    finally:
        connection.close()
