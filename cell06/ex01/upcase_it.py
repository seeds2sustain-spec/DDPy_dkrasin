#!/usr/bin/env python3

# กำหนดเมธอดชื่อ upcase_it ที่รับค่า string 1 ตัว
def upcase_it(text):
    # ส่งค่ากลับ (return) เป็นตัวพิมพ์ใหญ่ทั้งหมด
    return text.upper()

# ทดสอบการทำงานของเมธอดตามที่โจทย์ระบุ
print(upcase_it("hello"))
