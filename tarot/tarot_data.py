import os
import json

def load_tarot_data():
    if not os.path.exists('tarot_data.json'):
        print("Json data not found. Make sure its in the same directory")
        exit(1)
    with open('tarot_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

tarot_data = load_tarot_data()
