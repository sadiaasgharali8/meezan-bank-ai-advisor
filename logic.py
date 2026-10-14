import os
from dotenv import load_dotenv
from groq import Groq
from tools import (
    search_meezan_knowledge,
    get_usd_to_pkr_rate,
    get_prayer_times,
    get_gold_rate,
    get_account_balance,
)

# Load environment variables
load_dotenv()

# Initialize Groq Client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def get_ai_response(user_query: str) -> str:
    # Pehle knowledge base se context lo
    context = search_meezan_knowledge(user_query)

    # --- Live Tools Check ---
    query_lower = user_query.lower()

    # Gold rate (pehle check karo kyunki "rate" word common hai)
    if any(word in query_lower for word in ["gold", "sona"]):
        context += f"\n\nLive Data: {get_gold_rate()}"
    # Exchange rate
    elif any(word in query_lower for word in ["usd", "pkr", "dollar", "rate", "exchange", "currency"]):
        context += f"\n\nLive Data: {get_usd_to_pkr_rate()}"

    # Prayer times
    if any(word in query_lower for word in ["namaz", "prayer", "azan", "auqaat", "fajr", "isha"]):
        context += f"\n\nLive Data: {get_prayer_times()}"

    # Account balance
    if any(word in query_lower for word in ["balance", "kitne paise", "paisa"]):
        context += f"\n\nLive Data: {get_account_balance()}"
    # ------------------------

    if not client:
        return "API key nahi mili. Meharbani karke .env file mein GROQ_API_KEY check karein."

    prompt = f"""
    You are a helpful and professional AI Advisor for Meezan Bank. 
    Answer the user's question based on the provided Context.
    If live data is provided in the context, use it in your answer.
    If the answer is not in the context, politely say you don't have that information.
    Respond in a mix of Urdu (Roman) and English, keeping it professional.

    Context:
    {context}

    User Question: {user_query}
    """

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI model: {str(e)}"