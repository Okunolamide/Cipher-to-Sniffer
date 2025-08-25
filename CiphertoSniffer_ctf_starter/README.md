# Ethical Hacking CTF (Starter Pack)

This package contains beginner-friendly, **local-only** CTF challenges.
**For educational use. Do not deploy publicly.**

## Challenges
- Web: `challenges/web` (Flask app with intentional SQLi)
- Crypto: `challenges/crypto`
- Forensics: `challenges/forensics`
- Networking: `challenges/networking`
- Misc/OSINT: `challenges/misc`

## Quick Start (Web challenge)
```bash
cd challenges/web
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```