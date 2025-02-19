#GENERATE A BASIC CALCULATOR WITH HELP OF USER DEFINED FUNCTIONS

#(Q) CREATE A SIMPLE TO-DO LIST APPLICATION USING FUNCTIONS. WAP PROGRAM THAT ALLOWS A USER TO MANAGE A SIMPLE TO-DO LIST. THE PROGRAM SHOULD OFFER THE FOLLOWING FUNCTIONALITY.abs
d=0
def calculator():
    global d
    def task():
        global d
        i=0
        while i<5:
            global d
            print("************************************************\n")
            print("                CALCULATOR                      \n")
            print("************************************************\n")

            disp=print("1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE\n5.Clear\n6.Display\n7.EXIT")
            inp=input("Give input acording to the list of choice:")
            if inp=='add':
                def add():
                    global d
                    inp_task=int(input("\nEnter the number of operands you want to add:"))
                    i=1
                    while i<=inp_task:
                        add=int(input("Enter operand:"))
                        d+=add
                        print("The added value is:",d)
                        i+=1
                    print("The total value of addition is",d)
                add()
            elif inp=='sub':
                def sub():
                    global d
                    inp_task=int(input("\nEnter the number of operands you want to add:"))
                    i=1
                    while i<=inp_task:
                        sub=int(input("Enter operand:"))
                        d-=sub
                        print("The subtracted value is:",d)
                        i+=1
                    print("The total value of subtraction is",d)
                sub()
            elif inp=='multiply':
                def product():
                    global d
                    inp_task=int(input("\nEnter the number of operands you want to add:"))
                    i=1
                    while i<=inp_task:
                        mul=int(input("Enter operand:"))
                        d*=mul
                        print("The product value is:",d)
                        i+=1
                    print("The total value of multiplication is",d)
                product()
            elif inp=='divide':
                def divide():
                    global d
                    inp_task=int(input("\nEnter the number of operands you want to add:"))
                    i=1
                    while i<=inp_task:
                        div=int(input("Enter operand:"))
                        d/=div
                        print("The divided value is:",d)
                        i+=1
                    print("The total value of division is",d)
                divide()
            elif inp=='clear':
                def clear():
                    global d
                    if d!=0:
                        d=0
                        print("\nCLEARED\n")
                    elif len(d)==0:
                        print("\nNO TASK LEFT TO BE REMOVED\n")
                clear()
            elif inp=='disp':
                def disp():
                    print("The curent value if the calculation is:",d)
                disp()
            elif inp=='exit':
                print("\nEXITING CALCULATOR APPLICATION")
                break

    task()
calculator()
        
                

                
    
