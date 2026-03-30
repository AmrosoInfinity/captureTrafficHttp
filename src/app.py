import requests
import time
import uuid
import sys

def send_grab_track():
    # Konfigurasi Endpoint & Identitas (Data dari Android Device Anda)
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    fid = "c1qKYifWTW-I2eAyLBlnMj"
    auth_token = ("eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6ODc5MzcwMzk4NDI2OmFuZHJvaWQ6M"
                  "DU1ZTUxZTIyZmU0MzFkMjRmZDNlMyIsImV4cCI6MTc3NTM5NDc5OSwiZmlkIjoiYzFxS1lpZldUVy1J"
                  "mVBeUxCbG5NaiIsInByb2plY3ROdW1iZXIiOjg3OTM3MDM5ODQyNn0.AB2LPV8wRQIhAJZx0V5wmAY3"
                  "aGAPIpZFxGBLWaB8up1vzgZCfl0CGkboAiBgTqrLyz_XaaaM2qoC7rYJrQuv1GyQL0QdESHZ0wtK4g")

    session = requests.Session()
    
    # Headers mengikuti standar aplikasi mobile Grab
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Grab/5.230.0 (Android 11; Build/RP1A.200720.011)",
        "X-Grab-ID": fid,
        "X-Firebase-AppCheck": auth_token,
        "X-Request-Id": str(uuid.uuid4()),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

    # Data Payload (Form Data)
    data = {
        "event_name": "client_performance_log",
        "event_timestamp": int(time.time() * 1000),
        "event_uuid": str(uuid.uuid4()),
        "fid": fid,
        "app_version": "5.230.0",
        "platform": "Android"
    }

    print(f"[*] Menghubungi Target: {url}")
    print(f"[*] Menggunakan FID: {fid[:10]}...")

    try:
        # Kirim sebagai data (form-encoded)
        response = session.post(url, data=data, headers=headers, timeout=15)
        
        print(f"\n[+] SERVER RESPONSE")
        print(f"Status Code : {response.status_code}")
        print(f"Content Type: {response.headers.get('Content-Type')}")
        print(f"Body         : {response.text}")

        if response.status_code == 200:
            print("\n[SUCCESS] Token Valid & Format Diterima!")
        else:
            print(f"\n[FAILED] Server menolak dengan status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"\n[ERROR] Koneksi Gagal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    send_grab_track()
