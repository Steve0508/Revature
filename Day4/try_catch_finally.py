try:
    # file =open('data.txt','r')
    # data =file.read()
    # number=int(data)
    value=int(input("enter a number:"))
    result =10/value

except ZeroDivisionError:
    print(" divide by zero error")
except ValueError:
    print("Invalid data as input")
else:

    #Executed only if no exceptions occured
    print(f"Successfully divideed : {value}")

finally:
    #always executed, regardless of exception

    print("Project execution completed")
