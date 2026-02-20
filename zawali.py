# zawali.py  or  first cell in Colab
# Zawali Wisdom v0.1 – Tunisian budget coach 💸
# Ayoub 2026 – all rights yours

import random
import time

def print_slow(text, delay=0.03):
    """Print text like someone is typing – more natural feel"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Personality & fixed responses (this is your "data" for now)
responses = {
    "greeting": [
        "Salem ya zawali! Chbik chbik, kifach el flous el youm? 💸",
        "Ahla w sahla fi Zawali Wisdom – coach mta3 el 10 DT/day w zid!",
        "Ya weldi, t7eb n3awnek t3ich b 10 DT w tetfara7 b 500 millim?"
    ],
    "10dt": [
        "10 DT fi el youm? Possible! Pattern classique:\n"
        "- Café + bsissa / pain w zitouna = 2–2.5 DT\n"
        "- Lablabi ou harira men street = 3–4 DT\n"
        "- Pain + tomate + harissa lel 3cha = 1–2 DT\n"
        "Total: 6–8 DT w yebka fisa3 snack. Survive mode ON! 🔥",
        
        "Stratégie max saving: khobz kbir men four (1 DT), harissa men dar, w ma men bir. 3 DT max lel youm!"
    ],
    "fricassé": [
        "Fricassé rkhis fi:\n"
        "- Bab El Khadra / Sidi Boumendil (souvent 2–2.5 DT)\n"
        "- Vendors lel mdina m3a Marché Central\n"
        "Conseil: t7ott mayounnaize w harissa w makrouna men dar → double volume w half price.",
        
        "Dar: 3jina (1 DT), thon boite (2–3 DT), kartof w batata men souk → fricassé maison b 4–5 DT lel 4–5 personnes!"
    ],
    "makarouna": [
        "Makarouna t3ish 3 youm:\n"
        "Youm 1: makarouna b sel3a w 7soua normale\n"
        "Youm 2: salade makarouna berda (zid tomate, thon si 3andek, harissa)\n"
        "Youm 3: makarouna m7assra m3a 3asir tomate w wedja kif kif\n"
        "Portion kbir fi début → economy + no waste."
    ],
    "500millim": [
        "500 MILLIM TROUVÉ !!!! 🎉🎉\n"
        "Petit roi du jour. T7eb n9oulk: achri bonbon w zid fisa3 thé w zid 7lwa lel moral!",
        "Wouhouuu 500 millim = victoire zawali! Considère ça jackpot mta3 el pauvre 😂"
    ],
    "default": [
        "Mafhemtech chbik... Besm men 10 DT, fricassé, makarouna, lablabi, 500 millim w zid.",
        "Chnouwa el budget problem el youm ya sidi? 😏",
        "Donne-moi plus de détails w n7elloulek el mouchkil b zero flous!"
    ]
}

def get_response(user_text):
    text = user_text.lower().strip()
    
    if any(word in text for word in ["salem", "salut", "ahla", "chbik", "bonjour"]):
        return random.choice(responses["greeting"])
    
    elif "10" in text and ("dt" in text or "dinar" in text or "budget" in text or "youm" in text):
        return random.choice(responses["10dt"])
    
    elif "fricass" in text or "fricassé" in text or "fricassee" in text:
        return random.choice(responses["fricassé"])
    
    elif "makaroun" in text or "makrouna" in text or "pâtes" in text:
        return random.choice(responses["makarouna"])
    
    elif "500" in text and ("millim" in text or "coin" in text or "flous" in text):
        return random.choice(responses["500millim"])
    
    else:
        return random.choice(responses["default"])

# Main loop – chat until exit
print_slow("Zawali Wisdom v0.1 démarré... Tape 'exit' pour quitter.")
print_slow(random.choice(responses["greeting"]))

while True:
    user_input = input("Toi: ").strip()
    
    if user_input.lower() in ["exit", "bye", "quitter", "sortir", "chouf"]:
        print_slow("Maasalama ya zawali! Survive strong 💪💸")
        break
    
    if not user_input:
        continue
    
    response = get_response(user_input)
    print_slow(f"Zawali Wisdom: {response}")
