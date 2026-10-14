import requests
from data import get_knowledge_data


def search_meezan_knowledge(query: str) -> str:
    """
    Searches the Meezan Bank knowledge base for information relevant to the user's query.
    """
    knowledge = get_knowledge_data()
    query_lower = query.lower()
    return knowledge


def get_usd_to_pkr_rate() -> str:
    """Ye function internet se live USD to PKR exchange rate fetch karta hai."""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        pkr_rate = data["rates"]["PKR"]
        return f"Aaj ka live USD to PKR exchange rate: **1 USD = {pkr_rate} PKR** hai."
    except Exception as e:
        return f"Exchange rate fetch karne mein error aa gaya: {str(e)}"


def get_prayer_times() -> str:
    """Ye function Karachi ke liye aaj ki namaz ke auqaat fetch karta hai."""
    try:
        url = "https://api.aladhan.com/v1/timingsByCity?city=Karachi&country=Pakistan&method=1"
        response = requests.get(url)
        data = response.json()
        timings = data["data"]["timings"]
        return (
            f"Karachi ke liye aaj ki namaz ke auqaat: "
            f"Fajar: {timings['Fajr']}, Zuhr: {timings['Dhuhr']}, Asr: {timings['Asr']}, "
            f"Maghrib: {timings['Maghrib']}, Isha: {timings['Isha']}"
        )
    except Exception as e:
        return f"Prayer times fetch karne mein error aa gaya: {str(e)}"


def get_gold_rate() -> str:
    """Ye function live gold rate (PKR per gram) calculate karta hai."""
    try:
        # Gold price USD per ounce
        gold_response = requests.get("https://api.gold-api.com/price/XAU")
        gold_usd_oz = gold_response.json()["price"]

        # USD to PKR rate
        rate_response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        pkr_rate = rate_response.json()["rates"]["PKR"]

        # 1 ounce = 31.1035 grams
        gold_pkr_gram = (gold_usd_oz / 31.1035) * pkr_rate

        return f"Aaj ka live gold rate taqreeban **PKR {round(gold_pkr_gram, 2)} per gram** hai. (1 USD = {pkr_rate} PKR ke hisaab se)"
    except Exception as e:
        return f"Gold rate fetch karne mein error aa gaya: {str(e)}"


def get_account_balance() -> str:
    """Ye demo function ek dummy account balance return karta hai."""
    return (
        "Demo Account Details: Account Number: MZ-9876543210, Account Title: Danish Ahmed, "
        "Current Balance: PKR 250,000.00, Account Type: Meezan Bachat Account (Active). "
        "(Ye ek demo balance hai, asli balance ke liye Meezan mobile banking app use karein.)"
    )