import os
import streamlit as st
from agent_logic import run_agent

# 1. Page Configuration
st.set_page_config(page_title="Meezan Bank AI Advisor", page_icon="🏦", layout="centered")

# 2. Custom CSS
st.markdown("""
<style>
    .stChatInput > div > div > input { border: 2px solid #006633 !important; border-radius: 10px !important; }
    section[data-testid="stSidebar"] { background-color: #1a2a2a; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Setup
with st.sidebar:
    st.image("meezan_logo.png", width=150)
    st.markdown("---")
    st.markdown("### 🏦 About This Bot")
    st.info("Yeh AI Advisor Meezan Bank ki official information par based hai. Yeh aapko accounts, financing, aur services ke baray mein guide karega.")
    st.markdown("### ✨ Features")
    st.markdown("- ✅ 24/7 Availability")
    st.markdown("- ✅ Shariah-Compliant Info")
    st.markdown("- ✅ Instant Responses")
    st.markdown("- ✅ Live Tools (Rates, Prayer Times)")
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# 4. MAIN HEADING WITH LARGER LOGO (Centered)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image("meezan_logo.png", width=110)  # 👈 Size 65 se barha kar 110 kar diya
    st.markdown("<h1 style='text-align: center; color: #006633; font-size: 2.2rem; font-weight: bold; margin-bottom: 5px;'>Meezan Bank AI Advisor</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555; font-size: 1.1rem; margin-top: 0;'>Your Shariah-Compliant Banking & Financial Assistant</p>", unsafe_allow_html=True)

# 5. Image Mapping Function
def get_image_for_topic(query: str) -> str | None:
    q = query.lower()
    if any(w in q for w in ["bachat", "saving", "asaaan", "rosan", "account"]):
        return "images/bachat_account.png"
    elif any(w in q for w in ["car", "ijarah", "vehicle", "gaari", "auto"]):
        return "images/car_ijarah.png"
    elif any(w in q for w in ["home", "house", "ghar", "easy home"]):
        return "images/easy_home.png"
    elif any(w in q for w in ["app", "mobile", "internet", "online", "banking"]):
        return "images/mobile_app.png"
    elif any(w in q for w in ["interview", "job", "career", "naukri", "apply"]):
        return "images/interview_tips.png"
    elif any(w in q for w in ["dollar", "usd", "pkr", "rate", "currency"]):
        return "images/dollar_rate.png"
    elif any(w in q for w in ["gold", "sona"]):
        return "images/gold_rate.png"
    elif any(w in q for w in ["namaz", "prayer", "azan", "auqaat", "fajr", "isha"]):
        return "images/prayer_times.png"
    return None

# 6. Chat Initialization & Display
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Assalam-o-Alaikum! Main Meezan Bank ka AI Advisor hoon. Main aapki kya madad kar sakta hoon?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 7. Chat Input & AI Response
if prompt := st.chat_input("Ask about Accounts, Car Ijarah, or Investments...", key="main_chat"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Fetching Shariah-compliant info & live data..."):
            response = run_agent(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            img_path = get_image_for_topic(prompt)
            if img_path and os.path.exists(img_path):
                st.image(img_path, caption="📎 Related Information", use_container_width=True)