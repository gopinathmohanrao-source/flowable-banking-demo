FLOWABLE BANKING DEMO - Ready GitHub Repo (for Render deployment)
=================================================================

Contents
--------
- customer-api/app.py  -> GET /customer-finance/<custId>
- risk-api/app.py      -> POST /risk-record   (stores in-memory)
- requirements.txt
- render.yaml          -> Render blueprint (creates two web services)

Quick steps to use
------------------
1. Unzip this package.
2. Create a new GitHub repository (e.g. flowable-banking-demo).
3. From the repo root on your machine:
   git init
   git add .
   git commit -m "initial commit - flowable demo apis"
   git branch -M main
   git remote add origin https://github.com/<yourusername>/flowable-banking-demo.git
   git push -u origin main

4. On Render:
   - New -> Blueprint -> Connect to your GitHub repo -> Select this repo
   - Render will detect render.yaml and create two services (customer-api, risk-api)
   - Wait until both services show 'Healthy' (green)

5. Test endpoints (replace hostnames with the ones shown by Render):
   GET https://customer-api-xxxxx.onrender.com/customer-finance/C123
   POST https://risk-api-xxxxx.onrender.com/risk-record
     Body (JSON):
     {
       "customerId": "C123",
       "riskScore": 66,
       "flag": "HIGH",
       "comments": "Demo entry"
     }

Notes and troubleshooting
-------------------------
- Ensure the repo doesn't contain Maven/Java files (.mvn, mvnw, pom.xml).
- Use the exact render.yaml provided; it instructs Render to create two Python web services.
- If Render build fails, open the build logs. Typical fixes:
  * Missing requirements.txt (should be present at root)
  * Typos in startCommand (should be gunicorn <folder>.app:app)
- For Flowable HTTP tasks, use the full Render URLs returned after deployment.

Contact / Support
-----------------
If you face any errors during deployment, copy the Render build logs and paste them back here — I will diagnose and fix the repo or commands quickly.
