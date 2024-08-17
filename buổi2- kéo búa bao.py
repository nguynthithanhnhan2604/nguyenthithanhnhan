# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:31:13 2024

@author: DELL
"""

import random

print("Chào mừng bạn đến với trò chơi kéo - búa - bao!")

nguoi_chon = input("Nhập lựa chọn của bạn: ") 
if nguoi_chon == "kéo" or nguoi_chon == "búa" or nguoi_chon == "bao":
    print("Người chơi chọn: ", nguoi_chon)
    
    may_chon=random.choice(["kéo", "búa", "bao"]) 
    print("Máy chọn: ", may_chon)

    #Quy tắc chơi kéo - búa - bao
    if nguoi_chon==may_chon: 
        print("Hòa")
    elif (nguoi_chon=="kéo" and may_chon=="bao") or (nguoi_chon=="búa" and may_chon=="kéo") or (nguoi_chon=="bao" and may_chon=="búa"):
        print("Bạn thắng !")
    else:
        print("Bạn thua !")
else:
    print("Lỗi. Mời nhập lại")