import requests

def send_grab_track():
    url = "https://mcd-gateway.grabtaxi.com/v2/track"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Grab/5.230.0 (Android 11)",
        "X-Grab-ID": "giga-byte-tools-v1"
    }
    payload = {"event": "ping_test", "type": "capture_raw_text"}

    print(f"Mengirim ke: {url}")
    try:
        # Kita gunakan verify=False jika hanya untuk testing traffic 
        # (tapi Grab biasanya butuh SSL valid)
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Done! Status: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_grab_track()
