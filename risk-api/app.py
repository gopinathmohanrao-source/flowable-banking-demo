from flask import Flask, request, jsonify
import os

app = Flask(__name__)
records = []

@app.post("/risk-record")
def risk_record():
    data = request.get_json()
    # basic validation
    if not data:
        return jsonify({"status": "error", "message": "JSON body required"}), 400
    records.append(data)
    return jsonify({"status": "stored", "record": data})

@app.get("/records")
def get_records():
    return jsonify({"count": len(records), "records": records})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
