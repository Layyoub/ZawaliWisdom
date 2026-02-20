# zawali_ml.py – Zawali Wisdom v1: Generative ML Chatbot (English focus, expanded topics)
# All rights yours – customize freely

from transformers import pipeline, logging
import torch

logging.set_verbosity_error()  # Cleaner output

# Load small model (DistilGPT-2 – fast on CPU)
generator = pipeline('text-generation', model='distilgpt2', device=-1)  # -1 = CPU

# Personality & scope (updated for coffee, activities, Tunisian vibe)
system_prompt = """
You are Zawali Wisdom, a fun, street-smart Tunisian budget life coach in Tunis. 
Expertise ONLY: Low-budget life in Tunisia (Tunis area) – survive on 10 DT/day or less.
Cover:
- Cheap food (fricassé, makrouna, lablabi, brik...)
- Affordable coffee/tea spots (maqhas, cafés rkhis ~1-2 DT)
- Free/cheap activities (walk medina, souks, beaches, people-watching, free views in Sidi Bou Said, parks, haggling, louage hacks)
- Transport tips, small money wins (500 millim celebrations), motivation
Respond in simple casual English with Tunisian flavor (ya zawali, wouhou, emojis 💸💪). Keep short & useful.
If question is off-topic (not budget/fun in Tunisia), reply exactly: "Sorry ya sidi, that's outside my expertise. I'm your low-budget Tunis coach! Ask about cheap coffee, free activities, food hacks or saving tips."
"""

def generate_response(user_input):
    full_prompt = f"{system_prompt}\nUser: {user_input}\nZawali Wisdom:"
    response = generator(full_prompt, max_new_tokens=120, temperature=0.7, top_p=0.9, num_return_sequences=1)[0]['generated_text']
    ai_part = response.split("Zawali Wisdom:")[-1].strip()
    if len(ai_part) > 250:
        ai_part = ai_part[:250] + "..."
    return ai_part

print("Zawali Wisdom v1 ready! Type 'exit' to quit. Ask in English about budget stuff in Tunis 💸")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'exit':
        print("Maasalama, stay zawali-strong! 💪")
        break
    if not user_input:
        continue
    print(f"Zawali Wisdom: {generate_response(user_input)}")