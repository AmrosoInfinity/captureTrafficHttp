import requests
import time
import uuid
import json

def send_grab_track():
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    
    # Data dari device Android Anda
    FID = "c1qKYifWTW-I2eAyLBlnMj"
    AUTH_TOKEN = ("eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6ODc5MzcwMzk4NDI2OmFuZHJvaWQ6M"
                  "DU1ZTUxZTIyZmU0MzFkMjRmZDNlMyIsImV4cCI6MTc3NTM5NDc5OSwiZmlkIjoiYzFxS1lpZldUVy1J"
                  "mVBeUxCbG5NaiIsInByb2plY3ROdW1iZXIiOjg3OTM3MDM5ODQyNn0.AB2LPV8wRQIhAJZx0V5wmAY3"
                  "aGAPIpZFxGBLWaB8up1vzgZCfl0CGkboAiBgTqrLyz_XaaaM2qoC7rYJrQuv1GyQL0QdESHZ0wtK4g")

    current_ts = int(time.time() * 1000)
    
    # Struktur Payload Standar Grab Analytics
    payload = {
        "common": {
            "app_version": "5.230.0",
            "device_id": FID,
            "platform": "Android",
            "os_version": "11",
            "country_code": "ID",
            "language": "id"
        },
        "events": [
            {
                "event_name": "client_performance_log",
                "event_timestamp": current_ts,
                "event_uuid": str(uuid.uuid4()),
                "event_properties": {
                    "session_id": str(uuid.uuid4()),
                    "component": "giga_byte_tools",
                    "status": "active"
                }
            }
        ]
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "Grab/5.230.0 (Android 11; Build/RP1A.200720.011)",
        "X-Grab-ID": FID,
        "X-Firebase-AppCheck": AUTH_TOKEN,
        "X-Request-Id": str(uuid.uuid4()),
        "Accept-Encoding": "gzip, deflate"
    }

    print(f"[*] Target: {url}")
    try:
        # Menggunakan json= otomatis mengeset Content-Type ke application/json
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        print(f"\n[+] HASIL EKSEKUSI")
        print(f"Status: {response.status_code}")
        print(f"Body  : {response.text}")

        if response.status_code == 200:
            print("\n[OK] Payload Valid! Data diterima Grab.")
        elif response.status_code == 400:
            print("\n[!] Error 400: Struktur 'events' atau 'common' masih ada yang kurang.")
            
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    send_grab_track()
