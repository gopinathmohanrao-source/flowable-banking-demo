from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/customer-finance/<cust_id>")
def finance(cust_id):
    # mock data - adjust as needed
    data = {
        "customerId": cust_id,
        "avgBalance": 4200,
        "creditUtilization": 78,
        "lastMonthSuspiciousTx": 3
    }
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
