


#exception handling in  python allows you to gracefully manage



try:
    result=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")


    #############################
try:
    value=int(input("enter a number:"))
    result =10/value

except ValueError:
    print("Invalid input Please eneter a number..")
except ZeroDivisionError:
    print("Cannot divide by zero")




#handle multiple exceptions in one break
try:
    pass
except(ValueError,TypeError,ZeroDivisionError)as e:
    print(f"an error occured:{e}")
    