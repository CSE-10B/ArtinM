def convert_temp(): #recursion. 

    conversion = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ") #ask which conversion they want

    if conversion == "C" or conversion == "c": #if they want c to f
        c = int(input("Enter temperature in Celsius: "))
        f = c * 9 / 5 + 32 #formual, moved around a bit
        print(c , "C is" , int(f) , "in Fahrenheit")
        convert_temp()

    elif conversion == "F" or conversion == "f": #if they want f to c
        f = int(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9 #formula, moved around a bit
        print(f , "°F is"  , int(c) , "in Celsius")
        convert_temp()

    else:
        print("Invalid choice")

convert_temp()