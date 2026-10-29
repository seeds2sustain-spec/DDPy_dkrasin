#!/usr/bin/env python3

def array_of_names(persons_dict):
    full_names = []
    for first_name, last_name in persons_dict.items():
        # รวมชื่อและนามสกุลเข้าด้วยกัน พร้อมทำตัวอักษรแรกให้เป็นตัวพิมพ์ใหญ่
        full_names.append(f"{first_name.capitalize()} {last_name.capitalize()}")
    return full_names

# ส่วนทดสอบการทำงานของโปรแกรมตามตัวอย่างในโจทย์
if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    print(array_of_names(persons))
