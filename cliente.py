import socket
import random
import hashlib
import logging
import time
import * from _thread
import Thread from threading


def main():

    host = '192.168.1.5'
    puerto = 21
    idcliente = int(10000000*random.random())
    print('Hola, Cliente' + str(idCliente))
    logging.basicConfig(filename="./archivosC/cliente" + str(idcliente) + ".log", level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    print('Se terminó de configurar el log de su pronta conexión')
    hs = hashlib.sha256()
    print(hs)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("Se conecto satisfactoriamente con el host ",
          host, " en el puerto: ", port)
    sock.close()


main()
