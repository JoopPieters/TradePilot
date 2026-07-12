from datetime import datetime

from database.database import (
    maak_database,
    sla_scan_op,
    laatste_scans,
)

maak_database()

sla_scan_op(
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TEST",
    123.45,
    99,
    55.5,
)

print("Laatste scans:\n")

for scan in laatste_scans():
    print(scan)
