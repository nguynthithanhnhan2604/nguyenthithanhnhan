# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:08:27 2024

@author: DELL
"""

a=float(input(" Nhập số thực a:"))
b=float(input(" Nhập số thực b:"))
c=float(input(" Nhập số thực c:"))
delta= float(b**2-4*a*c)
if delta==0:
    print(" Phương trình có nghiệm kép:",-b/(2*a))
elif delta>0:
    print(" Phương trình có 2 nghiệm phân biệt:",(-b+ delta**2)/(2*a),"và",(-b- delta**2)/(2*a))
else:
    print(" Phương trình vô nghiệm ")