#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามา 1 ตัวพอดีหรือไม่ 
# (sys.argv ต้องมีความยาวเป็น 2 เพราะตำแหน่งที่ 0 คือชื่อไฟล์โปรแกรม)
if len(sys.argv) == 2:
    target_parameter = sys.argv[1]
    
    # แสดงข้อความถามและรับค่าจากผู้ใช้
    user_input = input("What was the parameter? ")
    
    # ตรวจสอบว่าคำที่ผู้ใช้พิมพ์ ตรงกับพารามิเตอร์หรือไม่
    if user_input == target_parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    # ถ้าพารามิเตอร์ที่ส่งมาไม่ใช่ 1 ตัว ให้พิมพ์ none
    print("none")