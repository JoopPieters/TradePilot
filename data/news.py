import os
import requests
from datetime import datetime, timedelta


def maak_nieuwsbericht(titel, bron, tijd, url, categorie):
    """Maak een gestandaardiseerd nieuwsbericht."""


    return {
        "titel": titel,
        "bron": bron,
        "tijd": tijd,
        "url": url,
        "categorie": categorie,
    }

ZOEKPROFIELEN = {
    "ASML.AS": [
        "ASML",
        "EUV",
        "High-NA",
        "lithography",
    ],

    "ASM.AS": [
    "ASM",
    "wafer equipment",
    "deposition",
    "atomic layer deposition",
],

    "BESI.AS": [
        "BESI",
        "BE Semiconductor",
        "die attach",
        "hybrid bonding",
        "advanced packaging",
    ],
}

def zoek_nieuws_term(zoekterm):
    """Zoek nieuws voor één afzonderlijke zoekterm via NewsAPI."""

    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("Fout: NEWS_API_KEY is niet ingesteld")
        return []

    url = "https://newsapi.org/v2/everything"

    parameters = {
        "q": zoekterm,
        "from": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
        "to": datetime.now().strftime("%Y-%m-%d"),
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": api_key,
    }

    try:
        antwoord = requests.get(url, params=parameters, timeout=10)
        antwoord.raise_for_status()

        gegevens = antwoord.json()

        if gegevens.get("status") != "ok":
            print("NewsAPI fout:", gegevens)
            return []

        return gegevens.get("articles", [])

    except Exception as fout:
        print(f"Fout bij ophalen nieuws: {fout}")
        return []

def zoek_nieuws(ticker):
    """Zoek nieuws voor een aandeel via het bijbehorende zoekprofiel."""

    zoektermen = ZOEKPROFIELEN.get(ticker, [ticker])

    nieuws = []
    bekende_urls = set()
    bekende_titels = set()

    for zoekterm in zoektermen:

        artikelen = zoek_nieuws_term(zoekterm)

        for artikel in artikelen:

            titel = artikel.get("title")
            url_artikel = artikel.get("url")

            if not titel or not url_artikel:
                continue

            titel_sleutel = titel.strip().lower()

            if not any(
                zoekterm.lower() in titel_sleutel
                for zoekterm in zoektermen
            ):
                continue

            if url_artikel in bekende_urls:
                continue

            if titel_sleutel in bekende_titels:
                continue

            bekende_urls.add(url_artikel)
            bekende_titels.add(titel_sleutel)

            nieuws.append(
                maak_nieuwsbericht(
                    titel,
                    artikel.get("source", {}).get("name"),
                    artikel.get("publishedAt"),
                    url_artikel,
                    "algemeen",
                )
            )

    return nieuws