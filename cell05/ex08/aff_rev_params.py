#!/usr/bin/env python3
import sys

# sys.argv นับชื่อไฟล์โปรแกรมเป็นตัวที่ 1 (index 0) 
# ถ้าต้องการพารามิเตอร์อย่างน้อย 2 ตัว ความยาวรวมของ sys.argv ต้องมีตั้งแต่ 3 ขึ้นไป
if len(sys.argv) < 3:
    print("none")
else:
    # วนลูปแบบย้อนกลับ เริ่มจากตำแหน่งสุดท้าย (len - 1) ถอยไปจนถึงตำแหน่งที่ 1 (หยุดก่อนถึง 0)
    for i in range(len(sys.argv) - 1, 0, -1):
        print(sys.argv[i])