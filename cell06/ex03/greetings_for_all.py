#!/usr/bin/env python3

# กำหนดเมธอด greetings โดยตั้งค่า default parameter เป็น "noble stranger"
def greetings(name="noble stranger"):
    # ตรวจสอบว่า type ของตัวแปร name เป็น string หรือไม่
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# ส่วนทดสอบโปรแกรมตามตัวอย่างในเอกสาร
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)