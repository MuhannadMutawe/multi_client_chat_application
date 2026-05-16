import socket
import threading

HOST = "127.0.0.1"
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                pass


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception()
            broadcast(message, client)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                # إرسال رسالة المغادرة بالعربية عبر الشبكة (هذا آمن ولا يسبب انهيار السيرفر)
                broadcast(f" {nickname} غادر الدردشة!".encode("utf-8"), client)
                nicknames.remove(nickname)
                break


def receive():
    print("Server is running and listening for connections...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f" {nickname} انضم للدردشة!".encode("utf-8"), client)
        client.send("تم الاتصال بنجاح!\n".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
