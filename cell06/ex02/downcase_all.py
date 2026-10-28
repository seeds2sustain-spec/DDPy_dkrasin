#!/usr/bin/env python3
import sys

# สร้างเมธอด downcase_it ตามที่โจทย์กำหนด
def downcase_it(text):
    # ส่งค่ากลับเป็นตัวพิมพ์เล็ก
    return text.lower()

# ตรวจสอบว่าไม่มีพารามิเตอร์ส่งเข้ามาเลยหรือไม่ (มีแค่ชื่อไฟล์โปรแกรม)
if len(sys.argv) == 1:
    print("none")
else:
    # วนลูปนำพารามิเตอร์แต่ละตัว (เริ่มตั้งแต่ index 1) เข้าไปในเมธอด downcase_it
    for param in sys.argv[1:]:
        # แสดงผลลัพธ์ที่ได้จากการ return ออกทางหน้าจอ
        print(downcase_it(param))