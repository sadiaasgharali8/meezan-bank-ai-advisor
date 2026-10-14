# Meezan Bank Knowledge Base Data

MEEZAN_KNOWLEDGE_BASE = """
1. Bank Overview:
- Meezan Bank Pakistan ka pehla aur sab se bada Islamic Commercial Bank hai.
- Mission: Premium Islamic banking services Shariah principles ke mutabiq provide karna.

2. Accounts (Bachat aur Current Accounts):
- Meezan Asaan Account: Kam documentation ke saath aasan account opening procedure.
- Meezan Bachat Account: Monthly profit payouts aur Halal savings options.
- Roshan Digital Account (RDA): Overseas Pakistanis ke liye online account aur investment options.

3. Financing & Loans (Consumer Finance):
- Car Ijarah: Shariah-compliant auto financing solution.
- Easy Home: Ghar khareedne, banane, ya renovate karne ke liye Islamic home financing.

4. Services & FAQs:
- Debit Cards, Mobile Banking App, Internet Banking, aur ATM network.
- Profit Calculator: Investment par Halal returns ki maloomat.
- Customer Support: Meezan Bank ki 24/7 Helpline number 111-333-777 hai (Pakistan se). Overseas se call karne ke liye +92-21-111-333-777 use karein.
1. Bank Overview:
- Meezan Bank Pakistan ka pehla aur sab se bada Islamic Commercial Bank hai.
- Mission: Premium Islamic banking services Shariah principles ke mutabiq provide karna.

2. Accounts (Bachat aur Current Accounts):
- Meezan Asaan Account: Kam documentation ke saath aasan account opening procedure.
- Meezan Bachat Account: Monthly profit payouts aur Halal savings options.
- Roshan Digital Account (RDA): Overseas Pakistanis ke liye online account aur investment options.

3. Financing & Loans (Consumer Finance):
- Car Ijarah: Shariah-compliant auto financing solution.
- Easy Home: Ghar khareedne, banane, ya renovate karne ke liye Islamic home financing.

4. Services & FAQs:
- Debit Cards, Mobile Banking App, Internet Banking, aur ATM network.
- Profit Calculator: Investment par Halal returns ki maloomat.

5. Interview & Recruitment (Jobs):
- Meezan Bank ka interview process 3 stages par mushtamil hai: (1) Online/Written Test, (2) HR Interview, (3) Technical/Panel Interview.
- Written test mein English, Math (quantitative), Analytical reasoning, aur Islamic banking basics ke sawal poochay jatay hain.
- Common interview questions: "Apne baare mein batayein", "Meezan Bank mein hi kyun apply kiya?", "Islamic banking aur conventional banking mein kya farq hai?", "Mudarabah aur Murabaha kya hai?"
- Islamic banking ki basic terms (Riba, Mudarabah, Murabaha, Ijarah, Musharakah) ki tayyari zaroor karein, kyunki interview mein in par sawal zaroor aate hain.
- Interview mein ye documents le kar jayen: CNIC, educational degrees aur marksheets, CV/resume, aur passport size pictures.
- Interview ke liye formal dress code behtar hai: light color shirt, dark trousers, aur saaf suthra libaas.
- Interview ke baad result aam tor par 1-2 haftay mein email ya phone par inform kiya jata hai.
- Jobs apply karne ke liye Meezan Bank ka official careers page visit karein: www.meezanbank.com/careers
"""

def get_knowledge_data():
    return MEEZAN_KNOWLEDGE_BASE
    # data.py

def load_knowledge():
    """Ye function knowledge.txt file se text parh kar return karta hai."""
    try:
        with open("knowledge.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Knowledge base file not found. Please check knowledge.txt"