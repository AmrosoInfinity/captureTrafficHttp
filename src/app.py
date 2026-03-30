import requests
import json

def send_grab_track():
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    
    # Payload simulasi (Sesuaikan dengan kebutuhan Anda)
    payload = {
        "event": "ping",
        "timestamp": 1710000000
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Grab/5.230.0 (Android 11)"
    }

    print(f"--- Mengirim request ke: {url} ---")
    try:
        # Menggunakan POST sesuai biasanya endpoint /track
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:100]}") # Print 100 karakter pertama
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_grab_track()
