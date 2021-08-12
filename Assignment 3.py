def Calculator(number1,number2,operator):
    if operator =='+':
        print(number1+number2)
    elif operator == '-':
        print(number1-number2)
    elif operator == '*':
        print(number1*number2)
    elif operator == '/':
        print(number1/number2)
    else:
        print("Invalid operator !")
        
def waterTempreture(degree):
    if degree >=100:
        print("Water boils!")
    elif degree >25 and degree <100:  
        print("Water is warming_up")
    elif degree ==25:
        print("Water in roomTempreture")
    elif degree <25  and degree >=0:
        print("Water is cooling_down")
    elif degree <0:
        print("Water Freezes!")
        
def slope(y1,x1,y2,x2):
    m=(y2-y1)/(x2-x1)
    if m >0:
        print("Slope is positive")
        print(" Slope= ",m)
    elif m<0:  
        print("Slope is negative")
        print(" Slope= ",m)
    elif m ==0:
        print("Slope is zero")
        print(" Slope= ",m)
    else:
        print("Slope is undefined")

# Constants cant be privet(able to be changed) in module
__constantSpeed=70        
        