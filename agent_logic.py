import os
import json
from groq import Groq
from tools import get_usd_to_pkr_rate, get_gold_rate, get_prayer_times, get_account_balance
from data import MEEZAN_KNOWLEDGE_BASE
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🛠️ Tool Definitions
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_usd_to_pkr_rate",
            "description": "Fetches the current USD to PKR exchange rate.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_gold_rate",
            "description": "Fetches the current gold rate in Pakistan.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_prayer_times",
            "description": "Fetches today's Islamic prayer times.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_account_balance",
            "description": "Checks the demo balance for a Meezan Bank account.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    }
]

# 🗺️ Map tool names to functions
AVAILABLE_TOOLS = {
    "get_usd_to_pkr_rate": get_usd_to_pkr_rate,
    "get_gold_rate": get_gold_rate,
    "get_prayer_times": get_prayer_times,
    "get_account_balance": get_account_balance
}

# 🧠 System Prompt
SYSTEM_PROMPT = f"""
You are Meezan Bank's AI Financial Advisor.
- Speak naturally in Roman Urdu and English.
- Use this knowledge base: {MEEZAN_KNOWLEDGE_BASE}
- If user asks for live rates or balance, YOU MUST USE THE TOOLS.
- Be professional and concise.
"""

def run_agent(user_query: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

    # Max 5 iterations to prevent infinite loops
    for _ in range(5):
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )
        msg = response.choices[0].message

        # Check if AI wants to use a tool
        if msg.tool_calls:
            messages.append(msg)
            for tool_call in msg.tool_calls:
                func_name = tool_call.function.name
                
                if func_name in AVAILABLE_TOOLS:
                    # Execute the tool
                    result = AVAILABLE_TOOLS[func_name]()
                    
                    # Send result back to AI
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": func_name,
                        "content": str(result)
                    })
        else:
            # AI is done and gave a final answer
            return msg.content

    return "Sorry, I couldn't process that request."