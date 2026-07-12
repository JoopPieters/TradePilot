import sqlite3
from pathlib import Path

DB_BESTAND = Path("database/tradepilot.db")


def maak_database():
    conn = sqlite3.connect(DB_BESTAND)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_datum TEXT,
        ticker TEXT,
        prijs REAL,

        score_day INTEGER,
        score_swing INTEGER,
        score_invest INTEGER,

        beste_strategie TEXT,
        oordeel TEXT,

        rsi REAL,
        ema20 REAL,
        ema50 REAL,
        macd REAL,
        signaal REAL
    )
    """)

    conn.commit()
    conn.close()


def sla_scan_op(
    scan_datum,
    ticker,
    prijs,

    score_day,
    score_swing,
    score_invest,

    beste_strategie,
    oordeel,

    rsi,
    ema20,
    ema50,
    macd,
    signaal,
):

    conn = sqlite3.connect(DB_BESTAND)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO scans(
        scan_datum,
        ticker,
        prijs,

        score_day,
        score_swing,
        score_invest,

        beste_strategie,
        oordeel,

        rsi,
        ema20,
        ema50,
        macd,
        signaal
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        scan_datum,
        ticker,
        prijs,

        score_day,
        score_swing,
        score_invest,

        beste_strategie,
        oordeel,

        rsi,
        ema20,
        ema50,
        macd,
        signaal,
    ))

    conn.commit()
    conn.close()


def laatste_scans(aantal=10):

    conn = sqlite3.connect(DB_BESTAND)
    cur = conn.cursor()

    cur.execute("""
    SELECT
        scan_datum,
        ticker,
        prijs,
        score_day,
        score_swing,
        score_invest,
        beste_strategie,
        oordeel
    FROM scans
    ORDER BY id DESC
    LIMIT ?
    """, (aantal,))

    rows = cur.fetchall()

    conn.close()

    return rows