import streamlit as st
from logic import get_ai_response

# --- 1. Page Configuration ---
st.set_page_config(page_title="Meezan Bank AI Advisor", page_icon="🏦", layout="centered")

# --- 2. Custom CSS for Meezan Bank Branding ---
st.markdown("""
<style>
    .main-header {
        color: #006633;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-header {
        color: #555;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 30px;
    }
    .stChatInput > div > div > input {
        border: 2px solid #006633 !important;
        border-radius: 10px !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #1a2a3a;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Sidebar ---
with st.sidebar:
        st.image("meezan_logo.png", width=150)
        
        st.markdown("---")
        
        st.markdown("### ℹ️ About This Bot")
        st.info("Yeh AI Advisor Meezan Bank ki official information par based hai. Yeh aapko accounts, financing, aur services ke baray mein guide karega.")
        
        st.markdown("---")
        
        st.markdown("### ✨ Features")
        st.markdown("- ✅ 24/7 Availability")
        st.markdown("- ✅ Shariah-Compliant Info")
        st.markdown("- ✅ Instant Responses")
        
        st.markdown("---")
        
        # Clear Chat Button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

# --- 4. Main Chat Interface ---
st.markdown('<div class="main-header">Meezan Bank AI Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your Shariah-Compliant Banking & Financial Assistant</div>', unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Assalam-o-Alaikum! Main Meezan Bank ka AI Advisor hoon. Main aapki kya madad kar sakta hoon?"}
    ]

# Display Chat Messages
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])
    else:
        with st.chat_message("user"):
            st.write(msg["content"])

# --- 5. Chat Input & Logic ---
if prompt := st.chat_input("Ask about Accounts, Car Ijarah, or Investments..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)
        
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking... Please wait."): 
            response = get_ai_response(prompt)
            st.write(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})