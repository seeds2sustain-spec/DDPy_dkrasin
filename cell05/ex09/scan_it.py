#!/usr/bin/env python3
import sys
import re

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามา 2 ตัวพอดีหรือไม่ 
# (sys.argv จะมีความยาวเป็น 3 เพราะ index 0 คือชื่อไฟล์โปรแกรม)
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    
    # ใช้ re.findall() ค้นหา keyword ใน search_string
    matches = re.findall(keyword, search_string)
    
    # ถ้าจำนวนที่ค้นเจอมีมากกว่า 0 ให้พิมพ์จำนวนครั้งออกมา
    if len(matches) > 0:
        print(len(matches))
    else:
        # ถ้าค้นหาไม่เจอเลย ให้พิมพ์ none
        print("none")
else:
    # ถ้าจำนวนพารามิเตอร์ไม่เท่ากับ 2 ตัว ให้พิมพ์ none
    print("none")