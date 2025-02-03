height=int(input("enter you height:"))
weight=int(input("enter you weight:"))
bmi = weight/ (height / 100) **2
if bmi <18.5:
    print("underweight")
elif 18.5 <=bmi <25:
    print("overweight")    
elif 25 <=bmi <30:
    print("overweight")    
elif 30 <= <35:
    print("obesity class 1")    
elif 35 <=bmi < 39.9:
    print("obesity class 2")    
else:
    print("super fat")    