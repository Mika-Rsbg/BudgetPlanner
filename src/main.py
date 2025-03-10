#!/usr/bin/env python3
# Dieses Beispielprogramm ruft die letzten 30 Tage der Konto-Historie ab.
# Voraussetzung: Installation der FinTS-Bibliothek: pip install fints
# Hinweis: Passe die Zugangsdaten und die FinTS-URL entsprechend an!

from fints.client import FinTS3PinTanClient
from datetime import date, timedelta

def get_account_history():
    # Ersetze die folgenden Werte mit Deinen tatsächlichen Bankdaten:
    fin_ts_url = "https://fints.sparkasse-aachen.de/fints"  # Beispiel-URL – ggf. anpassen
    bank_code = "39050000"   # Bankleitzahl der Sparkasse Aachen
    username = input("username:")  # Dein Benutzername
    pin = input("pin:")                # Deine PIN

    # Initialisieren des FinTS-Clients
    client = FinTS3PinTanClient(fin_ts_url, bank_code, username, pin)
    
    try:
        # Abrufen der SEPA-Konten (Kontenliste)
        accounts = client.get_sepa_accounts()
    except Exception as e:
        print("Fehler beim Abrufen der Konten:", e)
        return

    if not accounts:
        print("Keine Konten gefunden.")
        return

    # Für dieses Beispiel verwenden wir das erste Konto in der Liste
    account = accounts[0]
    print("Konto gefunden:", account)

    # Definiere den Zeitraum: letzte 30 Tage
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    
    try:
        # Abrufen der Transaktionen im definierten Zeitraum
        transactions = client.get_transactions(account, start_date, end_date)
    except Exception as e:
        print("Fehler beim Abrufen der Transaktionen:", e)
        return

    if not transactions:
        print("Keine Transaktionen im angegebenen Zeitraum gefunden.")
    else:
        print("Transaktionen der letzten 30 Tage:")
        for t in transactions:
            print(t)

if __name__ == '__main__':
    get_account_history()
