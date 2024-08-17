# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:43:33 2024

@author: DELL
"""

GPA=float(input("Nhập điểm trung bình GPA:"))
if GPA<3.5:
    print("Học lực Kém")
elif 3.5<=GPA<5:
    print("Học lực Yếu")
elif 5<=GPA<7:
    print("Học lực Trung bình")
elif 7<=GPA<8:
    print(" Học lực Khá")
elif 8<=GPA<9:
    print("Học lực Giỏi")
elif 9<=GPA<10:
    print("Học lực Xuất sắc")
else :
    print(" Không xác định")
        
    
          