from datetime import datetime
from pathlib import Path

LOGBESTAND = Path("logs/tradepilot.log")


def log(tekst):
    tijd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOGBESTAND, "a", encoding="utf-8") as f:
        f.write(f"[{tijd}] {tekst}\n")
