from gui.dashboard import start_dashboard

data = [
    {
        "ticker": "ASML.AS",
        "prijs": 711.45,
        "ema20": 702.12,
        "rsi": 58.2,
        "score": 91,
    },
    {
        "ticker": "INGA.AS",
        "prijs": 28.44,
        "ema20": 27.91,
        "rsi": 55.3,
        "score": 84,
    },
    {
        "ticker": "SHELL.AS",
        "prijs": 35.38,
        "ema20": 35.62,
        "rsi": 42.1,
        "score": 48,
    },
]

start_dashboard(data)
