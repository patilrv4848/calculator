from calcu import do_addition,do_substraction
def main():
    print("welcome to the calculator app")
    print("\n select the function") 
    print("1. Add") 
    print("2. substract")
    user_input =input("select the fuction: ")

    a=int(input ("value of A : "))
    b=int(input("value of B: "))

    if user_input == "1":
        result =do_addition(a,b)
    elif user_input == "2":
        result =do_substraction(a,b)
    
    print('Result:',result)
if __name__ == '__main__':
    main()