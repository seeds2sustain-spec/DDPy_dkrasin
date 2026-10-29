#!/usr/bin/env python3
import sys

# Get the number of parameters (subtracting 1 for the script name itself)
num_params = len(sys.argv) - 1

# Display the number of parameters followed by a newline
print(f"Number of parameters: {num_params}.")




# #!/usr/bin/env python3
# # บอกคอมพิวเตอร์ (ระบบปฏิบัติการ) ว่าให้รันไฟล์นี้ด้วยโปรแกรม Python 3

# import sys
# # เรียกใช้งานเครื่องมือเสริมที่ชื่อว่า 'sys' (system) 
# # เครื่องมือนี้จะช่วยให้โปรแกรมสามารถอ่านข้อมูลที่เราพิมพ์ต่อท้ายชื่อไฟล์ตอนที่สั่งรันโปรแกรมได้

# # Get the number of parameters (subtracting 1 for the script name itself)
# num_params = len(sys.argv) - 1
# # sys.argv คือกล่องที่เก็บคำสั่งทั้งหมดที่เราพิมพ์ตอนรันโปรแกรม (ซึ่งคำแรกสุดจะเป็น 'ชื่อไฟล์' เสมอ)
# # len(...) คือการนับว่าในกล่องนั้นมีข้อมูลทั้งหมดกี่ชิ้น
# # เราต้องนำมา ลบ 1 (- 1) เพื่อหัก 'ชื่อไฟล์' ออกไป จะได้เหลือแค่จำนวน "พารามิเตอร์" หรือข้อมูลที่เราส่งเข้าไปจริงๆ แล้วนำไปเก็บไว้ในตัวแปร num_params

# # Display the number of parameters followed by a newline
# print(f"Number of parameters: {num_params}.")
# # พิมพ์ข้อความ "Number of parameters: " ตามด้วยจำนวนที่นับได้ออกทางหน้าจอ
# # (ตัวอักษร f ด้านหน้าข้อความ ช่วยให้เราสามารถแทรกตัวแปร {num_params} ลงไปในประโยคได้เลย)