import requests
import subprocess

subprocess.check_call(['pip', 'install', 'requests'])

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency)

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        return amount * rate
    else:
        print(f"Konvertierung von {base_currency} zu {target_currency} nicht möglich.")
        return None

if __name__ == "__main__":
    amount = float(input("Betrag: "))
    base_currency = input("Von Währung (z. B. USD): ").upper()
    target_currency = input("Zu Währung (z. B. EUR): ").upper()

    result = convert_currency(amount, base_currency, target_currency)
    if result:
        print(f"{amount} {base_currency} = {result:.2f} {target_currency}")
