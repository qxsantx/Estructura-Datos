def mult (num1:float, num2:float)->float:
    if num1==0:
        return 0
    return num2+mult(num1-1,num2)
print(mult(8,6))