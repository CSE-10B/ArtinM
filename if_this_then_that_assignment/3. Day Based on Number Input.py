num = int(input())

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"] #list with all the days. 0-indexed

if 1 <= num <= 7: #if it's a valid day number, in bewteen 1 and 7 inclusive
    print(days[num - 1]) #subtract 1 to match the 0-indexed list
else:
    print("Invalid day number")
    
#To Mr. Jeffers:
#on canvas, you said this as an example: "if input = 1, output = Monday"
#in my thing, input of 2 results in an output of monday, as I went based on the Sunday to Saturday week cycle. 
#I did this before seeing the example, but the logic/code is basically the same, just the list is ordered differently