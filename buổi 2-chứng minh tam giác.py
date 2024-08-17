# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:14:40 2024

@author: DELL
"""
a=float(input(" Nhập cạnh của a:"))
b=float(input(" Nhập cạnh của b:"))
c=float(input(" Nhập cạnh của c:"))
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("a,b,c là 3 cạnh của tam giác và là tam giác đều")
    elif a == b or a == c or b == c:
        print("a,b,c là 3 cạnh của tam giác và là tam giấc cân")
    elif a**2+b**2==c**2 or a**2+b**2==c**2 or b**+c**2==a**2:
        print ("a,b,c là 3 cạnh của tam giác và là tam giác vuông")
    else:
        print("a,b,c là 3 cạnh của tam giác")
else:
        print("a,b,c không là 3 cạnh của tam giác")
        

    
    

        

            
            
        
        
      
      
   
        


