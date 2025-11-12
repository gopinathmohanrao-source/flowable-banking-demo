from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Customer API is running"}, 200


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

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

