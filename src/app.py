import requests
import time
import uuid
import json

def send_grab_track():
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    
    # DATA DARI DEVICE ANDA
    FID = "c1qKYifWTW-I2eAyLBlnMj"
    AUTH_TOKEN = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6ODc5MzcwMzk4NDI2OmFuZHJvaWQ6MDU1ZTUxZTIyZmU0MzFkMjRmZDNlMyIsImV4cCI6MTc3NTM5NDc5OSwiZmlkIjoiYzFxS1lpZldUVy1JMmVBeUxCbG5NaiIsInByb2plY3ROdW1iZXIiOjg3OTM3MDM5ODQyNn0.AB2LPV8wRQIhAJZx0V5wmAY3aGAPIpZFxGBLWaB8up1vzgZCfl0CGkboAiBgTqrLyz_XaaaM2qoC7rYJrQuv1GyQL0QdESHZ0wtK4g"

    current_ts = int(time.time() * 1000)
    event_uuid = str(uuid.uuid4())

    payload = {
        "events": [
            {
                "event_name": "client_performance_log",
                "event_timestamp": current_ts,
                "event_uuid": event_uuid,
                "event_properties": {
                    "fid": FID,
                    "platform": "Android",
                    "app_version": "5.230.0"
                }
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Grab/5.230.0 (Android 11; Build/RP1A.200720.011)",
        "X-Grab-ID": FID,
        "X-Firebase-AppCheck": AUTH_TOKEN, # Token Firebase yang Anda temukan
        "X-Request-Id": event_uuid
    }

    print(f"--- Mengirim request dengan Firebase Token ---")
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        
        if response.status_code == 200:
            print("BERHASIL: Token diterima oleh server.")
        else:
            print(f"Gagal: Server merespons {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_grab_track()
