
import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000



print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}")
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


s.close()