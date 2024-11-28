import requests
import time

def send_request():
    url = "http://server-container:5000"
    while True:
        payload = {"message": "What time is it?"}
        print("INFO: Client asked 'What time is it?'")
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print(f"INFO: Server answered Date: {data['date']}, Time: {data['time']}")
            else:
                print(f"INFO: Server responded with error: {response.text}")
        except Exception as e:
            print(f"INFO: Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    send_request()
