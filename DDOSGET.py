python3
import requests
import threading

def stress_test(url):
    while True:
        try:
            requests.get(url)
        except:
            pass

if __name__ == "__main__":
    url = input("Enter the URL of the website you want to stress test: ")
    num_threads = int(input("Enter the number of threads you want to use: "))

    for i in range(num_threads):
        thread = threading.Thread(target=stress_test, args=(url,))
        thread.start()


