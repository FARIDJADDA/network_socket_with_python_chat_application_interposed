
import socket
import time

# LOCALHOST : 127.0.0.1
HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024    



print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
# Boucle while qui tente de se reconnecter 
while True:
    try: 
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR: Impossible de se connecter au server. Reconnexion en cours...")
        time.sleep(5)
    else: 
        print("Connecté au serveur")
    break

# ....... utilisation de la socket

while True:
    data_recv = s.recv(MAX_DATA_SIZE)
    if not data_recv:
        break
    print(f"Message: {data_recv.decode()}")
    txt_send = input("Vous: ")
    s.sendall(txt_send.encode())
    
# .......
    
s.close()
