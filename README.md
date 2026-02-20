# ZawaliWisdom 💸

Tunisian low-budget life coach AI.  
Gives practical advice on surviving (and enjoying) life in Tunis on ~10 DT/day or less.

Focus areas:
- Cheap street food (fricassé, lablabi, makrouna hacks)
- Affordable coffee/tea maqhas
- Free or rkhis activities (medina walks, souks, beaches, haggling)
- Transport tips, small wins motivation (500 millim celebrations!)

Built with Python + Hugging Face Transformers (fine-tuned small LLM coming soon).

## Files
- `zawali.py`: Simple rule-based version
- `zawali_ml.py`: Generative ML version (prompt engineering + future fine-tune)
- `zawali_data.txt`: Training examples (upload soon)

Run locally:  
```bash
source zawali_env/bin/activate
python zawali_ml.py
