#!/usr/bin/env python3

# รับข้อความครั้งแรกจากผู้ใช้
user_input = input("What you gotta say? : ")

# วนลูปถามไปเรื่อยๆ ตราบใดที่สิ่งที่พิมพ์มาไม่ใช่คำว่า "STOP"
while user_input != "STOP":
    user_input = input("I got that! Anything else? : ")