from backtest.backtest import eenvoudige_backtest

resultaat = eenvoudige_backtest("ASML.AS")

if resultaat:
    print("\nBacktest\n")
    print(f"Ticker     : {resultaat['ticker']}")
    print(f"Aankoop    : € {resultaat['aankoop']:.2f}")
    print(f"Verkoop    : € {resultaat['verkoop']:.2f}")
    print(f"Rendement  : {resultaat['rendement']:.2f}%")
else:
    print("Geen gegevens.")
