#!/usr/bin/env python3

def famous_births(persons_dict):
    # นำค่า values ของดิกชันนารีมาเรียงลำดับโดยใช้คีย์ date_of_birth
    sorted_persons = sorted(persons_dict.values(), key=lambda x: x["date_of_birth"])

    # วนลูปเพื่อแสดงผลลัพธ์
    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# โค้ดทดสอบตามโจทย์
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)cd