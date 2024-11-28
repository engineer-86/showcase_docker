from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_time_and_date():
    data = request.get_json()
    if data.get("message", "").lower() == "what time is it?":
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        print(f"INFO: Client asked 'What time is it?' - Server answered Date: {current_date}, Time: {current_time}")
        return jsonify({"date": current_date, "time": current_time})
    print("INFO: Invalid request received")
    return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
