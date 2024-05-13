#addition 
def do_addition(a,b):
    return a+b
# substraction 
def do_substraction(a,b):
    return a-b
#divsion
def do_divsion(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return " can not divide by zero " 