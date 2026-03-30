import requests
import time
import uuid
import json

def send_grab_track():
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    fid = "c1qKYifWTW-I2eAyLBlnMj"
    # Token tetap sama
    auth_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6ODc5MzcwMzk4NDI2OmFuZHJvaWQ6MDU1ZTUxZTIyZmU0MzFkMjRmZDNlMyIsImV4cCI6MTc3NTM5NDc5OSwiZmlkIjoiYzFxS1lpZldUVy1JMmVBeUxCbG5NaiIsInByb2plY3ROdW1iZXIiOjg3OTM3MDM5ODQyNn0.AB2LPV8wRQIhAJZx0V5wmAY3aGAPIpZFxGBLWaB8up1vzgZCfl0CGkboAiBgTqrLyz_XaaaM2qoC7rYJrQuv1GyQL0QdESHZ0wtK4g"

    # Kita coba format FLAT (Tanpa 'common')
    payload = {
        "events": [
            {
                "event_name": "client_performance_log",
                "event_timestamp": int(time.time() * 1000),
                "event_uuid": str(uuid.uuid4()),
                "event_properties": {
                    "fid": fid,
                    "app_version": "5.230.0",
                    "platform": "Android",
                    "os_version": "11",
                    "network_type": "WIFI",
                    "request_id": str(uuid.uuid4())
                }
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Grab/5.230.0 (Android 11; Build/RP1A.200720.011)",
        "X-Grab-ID": fid,
        "X-Firebase-AppCheck": auth_token,
        "X-Request-Id": str(uuid.uuid4()),
        "Connection": "close" # Memaksa koneksi tutup setelah selesai untuk menghindari retransmission berlebih
    }

    print(f"[*] Mencoba Kirim Payload Flat...")
    try:
        # Gunakan json=payload agar requests menangani encoding UTF-8 secara otomatis
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        print(f"\n[+] SERVER RESPONSE")
        print(f"Status Code : {response.status_code}")
        print(f"Body         : {response.text}")

        if response.status_code == 200:
            print("\n[MANTAP] Akhirnya 200 OK!")
        else:
            # Jika masih gagal, kita kirim info tambahan
            print(f"[*] Tips: Coba cek capture_report.txt untuk melihat Hex Dump payload.")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    send_grab_track()
