
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(BASE_DIR, 'data', 'data.json')
os.makedirs(os.path.dirname(DATA_JSON), exist_ok=True)

def register_student_json(dictionary):
    register = read_student_json()
    register.append(dictionary)
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(register, f, ensure_ascii=False, indent=2)

def read_student_json():
    if not os.path.isfile(DATA_JSON):
        return []
    with open(DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def update_student_json(id_valor, campo_id, new_data):

    registerer = read_student_json()
    update = False
    for reg in registerer:
        if reg[campo_id] == id_valor:
            reg.update(new_data)
            update = True
            break
            
    if update:
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(registerer, f, ensure_ascii=False, indent=2)
            
    return update

def delete_student_json(id_valor, campo_id):

    register = read_student_json()
    news = [reg for reg in register if reg[campo_id] != id_valor]
    
    if len(news) != len(register):
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(news, f, ensure_ascii=False, indent=2)
        return True
        
    return False    

def search_student_id(id_valor, campo_id="id"): 

    register = read_student_json()
    for reg in register:
        if reg[campo_id] == id_valor:
            return reg
    return None
    
def search_student_name(name):
    register = read_student_json()
    results = []
    for reg in register:
        if name.lower() in reg["name"].lower():
            results.append(reg)
    return results
