# Web Challenge - Hidden Admin Panel (SQLi)

**Intentional vuln for CTF only. Run locally. Do NOT expose to the internet.**

## Run
```bash
cd challenges/web
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit: http://127.0.0.1:5000

## Goal
Bypass login via SQL Injection and view the flag on the admin page.

## Hint
Try inputs like `' OR '1'='1`

## Flag
FLAG{SQL_INJECTION_MASTER}