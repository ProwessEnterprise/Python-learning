def Add(a,b):
    return(a+b)   
def Sub(a,b):
    return(a-b)
def add_orsub():
    result = "no"
    while result=="no":
        user= input("+ or -: ")
        if result== "quit":
            print("yes, it's complete...")
        elif user== "+":
            print(Add(a=int(input()),b= int(input())))
        else:
            print(Sub(a=int(input()),b= int(input())))

        print("if you want to continue pls enter no / if you want to exit pls enter quit: ")
        result=input()
add_orsub()        