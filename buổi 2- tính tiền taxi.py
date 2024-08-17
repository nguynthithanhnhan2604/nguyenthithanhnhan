# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:06:28 2024

@author: DELL
"""
distance = float(input(" Nhập km đi được:"))
#km đầu tiên 
if distance ==1:
    tongtien=20
    print("Tổng tiền: ",tongtien )
# km thứ 
elif distance <=3 :
    tongtien=13*distance
    print("Tổng tiền: ",tongtien )
    #km thứ 4 đến 8
elif distance <= 8:
    tongtien= 3*13 + (distance -3)*12
    print("Tổng tiền: ",tongtien )
#Giá còn lại
else: 
    tongtien=3*13 + 5*12 + (distance - 8)*10 
    print("Tổng tiền: ",tongtien )
    # giảm giá
if tongtien>=100:
    tongtien= tongtien*0.9   
    print ("tổng tiền cần trả:", tongtien)
else:
    print (" Không xac dinh")