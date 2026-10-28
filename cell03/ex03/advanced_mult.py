#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีการใส่ข้อความอื่นต่อท้ายตอนรันโปรแกรมหรือไม่
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    # ลูปแรกสำหรับแม่สูตรคูณ (0 ถึง 10)
    while i <= 10:
        print(f"Table de {i}:", end="")
        j = 0
        # ลูปที่สองสำหรับตัวคูณ (0 ถึง 10)
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
        print() # ปัดขึ้นบรรทัดใหม่เมื่อจบแต่ละแม่
        i += 1