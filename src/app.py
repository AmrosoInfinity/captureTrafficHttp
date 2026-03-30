import requests
import time

def send_requests():
    print("--- Memulai pengiriman traffic HTTP ---")
    
    # Contoh request ke API publik
    targets = [
        "http://google.com",
        "http://httpbin.org/get",
        "http://example.com"
    ]
    
    for url in targets:
        try:
            response = requests.get(url, timeout=10)
            print(f"Request ke {url} | Status: {response.status_code}")
        except Exception as e:
            print(f"Gagal memanggil {url}: {e}")
        time.sleep(1)

if __name__ == "__main__":
    send_requests()
