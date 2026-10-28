#!/usr/bin/env python3
import math

# รับค่าตัวเลขจากผู้ใช้
num_str = input("Give me a number: ")

# แปลงข้อความเป็นทศนิยม (float) แล้วใช้ math.ceil() เพื่อปัดเศษขึ้นเป็นจำนวนเต็ม
rounded_num = math.ceil(float(num_str))

# แสดงผลลัพธ์
print(rounded_num)