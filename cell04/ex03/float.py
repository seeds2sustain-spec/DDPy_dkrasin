#!/usr/bin/env python3

number_str = input("Give me a number: ")

# แปลงข้อความให้เป็น float (ตามคำใบ้ Google string to float)
number_float = float(number_str)

# ตรวจสอบว่าตัวเลขนั้นเป็นจำนวนเต็มหรือไม่ (เช่น 42 หรือ 42.00)
if number_float.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")